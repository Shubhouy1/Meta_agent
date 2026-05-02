# Meta-Agent: AI System That Builds AI Agents

## Overview
Meta-Agent is an autonomous system that designs, generates, tests, and deploys AI agents from natural language descriptions using an end-to-end automated pipeline.

## Features
- What-if Simulation for tool selection  
- Self-Correction using LLM feedback  
- Pattern Learning for faster builds  
- Hybrid Architecture (LLM + prebuilt modules)  
- Automated Testing (syntax, imports, execution)  

## Architecture
Pipeline:
User Input -> Planner -> Tool Selector -> Code Generator -> Tester -> Deployer -> Working Agent

## Tech Stack
- LLM: Google Gemini 2.5 Flash  
- Embeddings: Google Embedding-001  
- Vector DB: ChromaDB  
- Framework: LangChain  
- UI: Streamlit  
- Language: Python 3.11+  

## Installation
```bash
git clone https://github.com/yourusername/meta-agent.git
cd meta-agent
pip install -r requirements.txt
echo "GOOGLE_API_KEY=your_api_key_here" > .env
streamlit run app.py
Usage

Describe the agent → Click "Build Agent" → System automatically generates and deploys it.

Team

Shubh Rastogi, Rahul Yadav, Ruchi Kumari, Surbhi Mahto, Madhumita Mandal


---

## ✅ Why this version is better

- Clean and short (perfect for submission)
- No formatting errors
- No broken code blocks
- Professional structure
- Easy for examiner to read quickly

---

## 🚀 Now just do:

```bash
git add README.md
git commit -m "Added clean README"
git push
