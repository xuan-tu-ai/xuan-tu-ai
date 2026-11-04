"""Render the last year of GitHub contributions as light and dark SVG grids (no snake)."""
import json, os, sys, urllib.request

LEVELS = ["NONE", "FIRST_QUARTILE", "SECOND_QUARTILE", "THIRD_QUARTILE", "FOURTH_QUARTILE"]
THEMES = {
    "light": {"cells": ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"], "text": "#57606a"},
    "dark": {"cells": ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"], "text": "#8b949e"},
}
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
CELL, GAP, LEFT, TOP = 11, 3, 30, 20

QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{date weekday contributionCount contributionLevel}}}}}}"""


def fetch(login, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    data = json.load(urllib.request.urlopen(req))
    if "errors" in data:
        sys.exit(data["errors"])
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def render(cal, theme):
    t = THEMES[theme]
    weeks = cal["weeks"]
    width = LEFT + len(weeks) * (CELL + GAP) + 10
    height = TOP + 7 * (CELL + GAP) + 26
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
           f'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif" font-size="10">']
    last_month = None
    for i, week in enumerate(weeks):
        x = LEFT + i * (CELL + GAP)
        month = int(week["contributionDays"][0]["date"][5:7])
        if month != last_month and i < len(weeks) - 2:
            out.append(f'<text x="{x}" y="{TOP - 7}" fill="{t["text"]}">{MONTHS[month - 1]}</text>')
            last_month = month
        for day in week["contributionDays"]:
            y = TOP + day["weekday"] * (CELL + GAP)
            fill = t["cells"][LEVELS.index(day["contributionLevel"])]
            n = day["contributionCount"]
            out.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}">'
                       f'<title>{n} contribution{"" if n == 1 else "s"} on {day["date"]}</title></rect>')
    for wd, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        out.append(f'<text x="0" y="{TOP + wd * (CELL + GAP) + 9}" fill="{t["text"]}">{name}</text>')
    ly = TOP + 7 * (CELL + GAP) + 12
    out.append(f'<text x="{LEFT}" y="{ly + 9}" fill="{t["text"]}">{cal["totalContributions"]} contributions in the last year</text>')
    lx = width - 10 - 5 * (CELL + GAP) - 64
    out.append(f'<text x="{lx}" y="{ly + 9}" fill="{t["text"]}">Less</text>')
    for k, c in enumerate(t["cells"]):
        out.append(f'<rect x="{lx + 28 + k * (CELL + GAP)}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" fill="{c}"/>')
    out.append(f'<text x="{lx + 30 + 5 * (CELL + GAP)}" y="{ly + 9}" fill="{t["text"]}">More</text>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    login, outdir = sys.argv[1], sys.argv[2]
    cal = fetch(login, os.environ["GITHUB_TOKEN"])
    os.makedirs(outdir, exist_ok=True)
    for theme in THEMES:
        name = "contribution-grid.svg" if theme == "light" else "contribution-grid-dark.svg"
        with open(os.path.join(outdir, name), "w") as f:
            f.write(render(cal, theme))
