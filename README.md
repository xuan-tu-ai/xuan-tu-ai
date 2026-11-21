<h1 align="center">Hi 👋, I'm Nguyễn Xuân Tự</h1>

<p align="center">
 <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=24&duration=3000&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=AI+Engineer+%40+Data+Impact;Vision-Language-Action+Robotics;Computer+Vision+%26+Industrial+AI;MLOps+%7C+Docker+%2B+Databricks" />
</p>

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmt2Z20waXF3Z2czZmxmN3p1dmJmZjJzZ2VhbXY3djluN2YweDRxdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EZr27ZbJwmjE9PGyLN/giphy.gif" width="250" alt="coding" />
</p>

<p align="center">
  <a href="mailto:nxuantu36@gmail.com"><img src="https://img.shields.io/badge/Email-F54A4A?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/xuan-tu-ai"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/nguy%E1%BB%85n-xu%C3%A2n-t%E1%BB%B1-489541248/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
</p>

---

## 🧠 About Me

- 🤖 **AI Engineer at Data Impact** (Hanoi) since Sep 2026, after a 5-month internship there. I build computer vision, robotics and anomaly detection systems for manufacturing clients in Thailand and Japan.
- 🎓 **B.Sc. in Management Information Systems**, Hanoi University of Science and Technology (HUST), CPA **3.4/4.0**.
- 🔬 Researcher at **SAMI-HUST** (ML Scientific Working Group): co-authoring a paper on ordinal fish freshness grading (FocalCORN-Swin) that reaches **90.01%** accuracy on the FFE benchmark (mean of 10 seeds), **5.6 points** above a matched re-run of the previous best pipeline, with a third of the calibration error of cross-entropy baselines.
- 📈 Previously: Data Scientist Intern at the Institute of Energy Technology (HUST), forecasting and anomaly detection for a solar power plant; TEEP intern at Asia University and student researcher at XiangQi Technology, Inc. (Taiwan), receiving the 2024 TEEP **Special Performance Award**.
- 🌏 TOEIC **930**; fluent in English and Chinese.
- 🌱 Interested in Vision-Language-Action models, model interpretability, and MLOps (Docker, FastAPI, Databricks, Vertex AI).

## 🚀 My Featured Projects

_Projects in agentic AI, robotics, computer vision, applied ML and full-stack apps, grouped by area._

#### 🧠 Agentic AI & Context

| Repository | Description | Topics |
|---|---|---|
| [**dsh-carryon**](https://github.com/xuan-tu-ai/dsh-carryon) | TypeScript port of carrycode's CarryOn runtime as a compaction plugin for DeepSeek Harness: long sessions are folded into validated, versioned records instead of a free-text summary, plus a CarryOn mode in the Web UI. **0.1.0 waits on a real-model release gate.** | `dsh-plugin` `context-management` `typescript` |
| [**carrycode**](https://github.com/xuan-tu-ai/carrycode) | Open implementation of *Pack Light, CarryOn* ([arXiv:2610.18784](https://arxiv.org/abs/2610.18784)), wrapped as a coding agent you run in your own repository. Old history is replaced by a compact, structured checkpoint of the agent's progress; recent steps stay verbatim. Built on mini-swe-agent, with a SWE-bench Verified evaluation harness. **Experimental.** | `coding-agent` `context-management` `llm-agents` `python` |
| [**harness-audit**](https://github.com/xuan-tu-ai/harness-audit) | Checks whether a change to an agent harness really made the agent better, with a verdict on each of the four claims a reported improvement rests on. | `agent-evaluation` `llm-agents` `statistics` `python` |

#### 🦾 Physical AI & Robotics

| Repository | Description | Topics |
|---|---|---|
| **Vision-Language-Action Robot Arm** 🔒 | Company project at Data Impact: fine-tuned VLA policies (**XVLA**, then **SmolVLA**) with **LeRobot** on an SO-ARM-101 arm for cup picking and pouring, served over gRPC from a GPU server, then an **ACT** policy for a bottle-pouring live demo. A mechanistic interpretability toolkit (cross-attention maps, SigLIP feature maps, weight-diff, FFN neuron probing) diagnoses failures, and a **YOLOv11** safety module freezes the robot when a person enters the frame. *Code is private.* | `vla` `lerobot` `interpretability` `pytorch` |
| **Arm + Hand Skill Orchestrator** 🔒 | SO-ARM-101 arm and AmazingHand dexterous hand on one stand performing a 6-step cup handover. Each step is its own **ACT** policy; a fine-tuned small vision-language model (**LFM-VL**) acts as a judge that watches both cameras and decides when a step is done. Explainability for the judge (occlusion maps, per-layer attention hooks, gradient×attention, logit lens) shows where it looks and why it sometimes passes a step too early; the ACT policies get camera/state ablation and occlusion analysis. *Code is private.* | `robotics` `act` `vlm` `xai` |
| **World Models for Failure Detection** 🔒 | Action-conditioned world models of the handover task that predict upcoming camera states: **LeWM** (trained end to end) and a DINO-WM-style predictor (**PreJEPA**) on frozen **V-JEPA 2.1** tokens. They flag failed runs by "surprise" (the real camera drifting from the prediction), and a pixel decoder shows what the model imagines. *Code is private.* | `world-model` `jepa` `v-jepa` `pytorch` |

#### 👁️ Computer Vision & Applied ML

| Repository | Description | Topics |
|---|---|---|
| **Robot Sensor Anomaly Detection** 🔒 | Company project at Data Impact for a manufacturing client in Japan: weakly supervised (**Multiple Instance Learning**) anomaly detection on multivariate robot sensor time series encoded as images (GAF, MTF, recurrence plots), built on **Databricks/PySpark** (Azure). Sanity baselines I designed exposed a data-leakage risk (PR-AUC 0.77 vs. a 0.29 random floor), which informed a go/no-go decision. *Code is private.* | `anomaly-detection` `multiple-instance-learning` `time-series` `databricks` |
| **Ordinal Fish-Eye Freshness (paper code)** 🔒 | Research code for the SAMI-HUST paper on the FFE benchmark: fish-eye freshness framed as **ordinal** classification, a **Swin-Tiny** backbone with a **focal CORN** head. Selection is kept apart from evaluation: one fixed species-stratified test split, five-fold CV on the development set, a separate **Optuna** (TPE + Hyperband) search per candidate, then final models over ten training seeds evaluated once on the test set. *Code is private until the paper is published.* | `pytorch` `ordinal-regression` `swin-transformer` `optuna` |
| [**fresheye**](https://github.com/xuan-tu-ai/fresheye) | Mobile-first web app built on the paper's model (graduation thesis): grades a fish from eye photos with an **EigenCAM** overlay and a **kNN strangeness score**, then a deterministic rule decides to *answer*, *ask for another photo* or *abstain*. A tool-calling LLM agent (Gemini or local Ollama) explains results in Vietnamese. FastAPI + React 19/TypeScript, served on one port. Earlier prototypes: [Streamlit](https://github.com/xuan-tu-ai/fish-freshness-classification-web), [FastAPI + Next.js](https://github.com/xuan-tu-ai/fish-freshness-classification-app). | `computer-vision` `fastapi` `react` `llm-agents` |

#### 📚 EdTech & Full-stack

| Repository | Description | Topics |
|---|---|---|
| [**Readly**](https://github.com/xuan-tu-ai/Readly) | AI-guided reading app for Vietnamese grade-12 literature: staged questions with rubric-based AI feedback, streaks and badges, teacher dashboards with a class highlight map, and AI-drafted content for admins. Next.js 16 + PostgreSQL with a pg-boss worker, installable as a PWA. **[Live demo](https://readly-production-3cec7280.up.railway.app)**. | `nextjs` `typescript` `postgresql` `llm` `edtech` |

#### 🛠️ Developer Tools & MLOps

| Repository | Description | Topics |
|---|---|---|
| [**kgrun**](https://github.com/xuan-tu-ai/kgrun) | CLI that runs a local Python script on free Kaggle GPUs (2× T4) with one command, through the official Kaggle API. | `mlops` `kaggle` `gpu` `cli` `python` |

---
### 🧠 My Core Expertise & Technical Skills

My skill set is centered around the AI/ML ecosystem, with a strong supporting foundation in web technologies and a focus on efficient tooling.

- **🤖 AI, Machine Learning & Data Science:**
  <p align="left">
    <a href="https://skillicons.dev">
      <img src="https://skillicons.dev/icons?i=python,pytorch,sklearn,anaconda,opencv&cache_bust=1" />
    </a>
  </p>

- **🌐 Web Development & Deployment:**
  <p align="left">
    <a href="https://skillicons.dev">
      <img src="https://skillicons.dev/icons?i=js,react,tailwind,vite,nextjs,nodejs,fastapi,docker,supabase,aws&cache_bust=1" />
    </a>
  </p>
  
- **🛢️ Languages, Databases & Tools:**
  <p align="left">
    <a href="https://skillicons.dev">
      <img src="https://skillicons.dev/icons?i=c,bash,postgresql,mongodb,git,github,vscode,pycharm&cache_bust=1" />
    </a>
  </p>
  
## 📊 GitHub Stats

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api?username=xuan-tu-ai&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true" />
    <source media="(prefers-color-scheme: light)" srcset="https://github-stats-extended.vercel.app/api?username=xuan-tu-ai&show_icons=true&theme=default&include_all_commits=true" />
    <img alt="GitHub Stats" src="https://github-stats-extended.vercel.app/api?username=xuan-tu-ai&show_icons=true&theme=tokyonight&include_all_commits=true" height="165" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=xuan-tu-ai&theme=tokyonight&hide_border=true" />
    <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com/?user=xuan-tu-ai&theme=default" />
    <img alt="GitHub Streak" src="https://streak-stats.demolab.com/?user=xuan-tu-ai&theme=tokyonight" height="165" />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api/top-langs/?username=xuan-tu-ai&layout=compact&theme=tokyonight&hide_border=true&hide=css,html,shell,dockerfile" />
    <source media="(prefers-color-scheme: light)" srcset="https://github-stats-extended.vercel.app/api/top-langs/?username=xuan-tu-ai&layout=compact&theme=default&hide=css,html,shell,dockerfile" />
    <img alt="Top Languages" src="https://github-stats-extended.vercel.app/api/top-langs/?username=xuan-tu-ai&layout=compact&theme=tokyonight&hide_border=true&hide=css,html,shell,dockerfile" height="150" />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/xuan-tu-ai/xuan-tu-ai/output/contribution-grid-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/xuan-tu-ai/xuan-tu-ai/output/contribution-grid.svg" />
    <img alt="GitHub contributions in the last year" src="https://raw.githubusercontent.com/xuan-tu-ai/xuan-tu-ai/output/contribution-grid.svg" />
  </picture>
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=36BCF7&height=100&section=footer"/>
</p>
