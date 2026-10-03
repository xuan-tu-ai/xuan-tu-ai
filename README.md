<h1 align="center">Hi 👋, I'm Nguyễn Xuân Tự (Lucas)</h1>

<p align="center">
 <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=24&duration=3000&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=AI+Engineer+%40+Data+Impact;Vision-Language-Action+Robotics;Computer+Vision+%26+Industrial+AI;MLOps+%7C+Docker+%2B+Databricks" />
</p>

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmt2Z20waXF3Z2czZmxmN3p1dmJmZjJzZ2VhbXY3djluN2YweDRxdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EZr27ZbJwmjE9PGyLN/giphy.gif" width="250" alt="coding" />
</p>

<p align="center">
  <a href="mailto:nxuantu36@gmail.com"><img src="https://img.shields.io/badge/Email-F54A4A?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/xuan-tu-ai"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/huy-t%E1%BB%B1-489541248/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
</p>

---

## 🧠 About Me

- 🤖 **AI Engineer** at **Data Impact** (Hanoi), full-time since Sep 2026 after a 5-month internship. I build computer vision, robotics, and anomaly detection systems for manufacturing clients in Thailand and Japan.
- 🎓 Final-year MIS student at **Hanoi University of Science and Technology (HUST)**.
- 🔬 Member of **ML Scientific Working Group (SAMI-HUST)**, co-authoring research on fish freshness classification (**88.4%** accuracy on the FFE dataset, above the previous 85.99% benchmark).
- 📈 Former **Data Scientist Intern** at Institute of Energy Technology (HUST), working on time-series forecasting and anomaly detection for a solar power plant.
- 🌏 **Ex-TEEP Intern** at Asia University & Student Researcher at **XiangQi Technology, Inc.** (Taiwan).
- 🏆 Awarded **Special Performance Award** for 2024 TEEP Program.
- 💬 TOEIC: **930** | Fluent in English & Spoken Chinese.
- 🌱 Interested in Vision-Language-Action models, model interpretability, and deploying AI systems with **MLOps** (Docker, FastAPI, Databricks, Vertex AI).

## 🚀 My Featured Projects

_A selection of projects where I applied my skills in computer vision and machine learning to solve real-world problems._

### 🦾 Vision-Language-Action Robot Arm (Data Impact)
> **Project Type:** Company project
>
> I deployed **SmolVLA** with the **LeRobot** framework on an SO-ARM-101 robot arm, using client-server (gRPC) inference on an RTX 4060 Ti GPU, and trained a working pouring policy (200k steps). After diagnosing a frozen text encoder as the grounding bottleneck of the previous XVLA model, I led the switch to SmolVLA and built a **mechanistic interpretability toolkit** (cross-attention maps, SigLIP feature maps, weight-diff, FFN neuron probing) to debug robot behavior. I also designed a **YOLOv11**-based safety module that freezes the robot when a person enters the camera frame.
>
> <sub>**Tech:** PyTorch, LeRobot, Hugging Face, SigLIP, YOLOv11, gRPC, Weights & Biases</sub>  
> 🔒 *Company project: code is private.*

### 🏭 Warehouse Forklift Safety Analytics (Data Impact)
> **Project Type:** Company project for a manufacturing client in Thailand
>
> I built a pipeline that detects unsafe forklift behavior from fixed CCTV cameras using **YOLO11** pose/detection and **ByteTrack**. A pixel-budget analysis (only 3.8% of frames usable) ruled out an ear-based head-pose approach before any model work. I delivered metric pedestrian-forklift proximity zones from a single camera (**R² = 0.912**), cut false-positive detections from **10/279 to 0/279** frames with a motion filter, and shipped a Streamlit demo.
>
> <sub>**Tech:** Python, YOLO11, ByteTrack, OpenCV, NumPy, Streamlit</sub>  
> 🔒 *Company project: code is private.*

### ⚙️ Industrial Sensor Anomaly Detection (Data Impact)
> **Project Type:** Company project for a manufacturing client in Japan
>
> I owned an independent research track on weakly supervised (**Multiple Instance Learning**) anomaly detection for multivariate robot sensor time series encoded as images (GAF, MTF, recurrence plots), built on **Databricks/PySpark** (Azure). Sanity baselines I designed exposed a **data-leakage risk** (PR-AUC 0.77 vs. 0.29 random floor), which informed a go/no-go decision. The codebase has 38 integration tests and a YAML config system.
>
> <sub>**Tech:** Databricks, PySpark, Azure, PyTorch, NumPy, pytest</sub>  
> 🔒 *Company project: code is private.*
### 📹 Real-time Violence Detection & Interpretation System
> **Competition:** AI Thuc Chien 2025 (Gen Viet Team)
>
> As the Team Leader and MLOps Engineer, I built an end-to-end multi-threaded pipeline integrating **YOLOv8n** (Tracking), **VideoMAE** (Action Recognition), and a **Small Language Model (SLM)** to detect and describe violent behaviors in real-time. I engineered an **automated data annotation pipeline** utilizing pseudo-labeling techniques to process 1,000 videos from the RLVS dataset, generating high-quality text captions for training without manual effort. The entire system was containerized using **Docker** and deployed as **FastAPI** endpoints on **Google Vertex AI** to serve the frontend interface, ensuring scalability and seamless interaction.
>
> <sub>**Tech:** Python, YOLOv8n, VideoMAE, Docker, FastAPI, Google Vertex AI</sub>  
> ➡️ **[View Project Details](https://github.com/xuan-tu-ai/ViolenceDetectionApp)**
> 
### 🗓️ UniSync – Student Schedule Management Solution
> **Competition:** NAVER Vietnam AI Hackathon 2025
>
> I engineered a productivity platform featuring a **Natural Language Processing (NLP)** parser that automates complex event scheduling from unstructured Vietnamese text. By integrating **Gemini 1.5 Flash**, the system performs intelligent data extraction to convert user prompts into structured calendar events. It utilizes **Supabase** for real-time synchronization and is deployed on **Vercel** as a scalable, low-latency solution.
>
> <sub>**Tech:** React, TypeScript, Gemini AI, Supabase, Vercel, Vite</sub>

> ➡️ **[View Project Details](https://github.com/xuan-tu-ai/naver-vietnam-ai-hackathon-XuanTu2002)**

### 📈 FinBERT-VCSenti: Financial Sentiment Analysis
> **Project Type:** Personal Project
>
> I fine-tuned a `bert-base-uncased` model for sentiment analysis on financial texts using PyTorch and Hugging Face Transformers. By processing and training on the Financial PhraseBank dataset, the model achieved an **Accuracy of 85.5%** and an **F1-Score of 85.5%** on the test set. I then deployed the model as an API service using FastAPI and Docker, making it publicly available for interactive testing on Hugging Face Spaces.
>
> <sub>**Tech:** PyTorch, Hugging Face Transformers, FastAPI, Docker</sub>  
> ➡️ **[View Project Details](https://github.com/xuan-tu-ai/FinBERT-VCSenti)**

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
  <img src="https://github-readme-stats.vercel.app/api?username=xuan-tu-ai&show_icons=true&theme=radical&count_private=true" width="47%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=xuan-tu-ai&layout=compact&theme=radical&count_private=true&hide=css,html,shell,dockerfile" width="47%" />
</p>

---

## 📫 Connect with Me

<p align="center">
  <a href="mailto:nxuantu36@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/xuan-tu-ai"><img src="https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white" /></a>
   <a href="https://www.linkedin.com/in/huy-t%E1%BB%B1-489541248/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=36BCF7&height=100&section=footer"/>
</p>
