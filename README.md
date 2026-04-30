# Meta-Agent: AI System That Builds AI Agents

## Overview

Meta-Agent is an autonomous system that designs, generates, tests, and deploys AI agents from natural language descriptions. Users simply describe the agent they want, and Meta-Agent handles planning, tool selection, code generation, testing, and deployment automatically.

## Key Innovations

1. What-if Simulation - Compares all tool options before selection with objective scoring
2. Self-Correction - LLM receives error feedback and fixes its own code
3. Pattern Learning - Caches successful patterns for faster future builds
4. Hybrid Architecture - LLM for intelligence, prebuilt for reliability
5. Auto Testing - 4-stage validation (syntax, imports, structure, execution)

## Architecture

The system follows a 5-stage pipeline:

User Input -> Planner -> Tool Selector -> Code Generator -> Tester -> Deployer -> Working Agent

- Stage 1: Planner - LLM analyzes request and determines agent type
- Stage 2: Tool Selector - What-if simulation compares all tool implementations
- Stage 3: Code Generator - LLM generates code with self-correction loop
- Stage 4: Tester - 4-stage automated validation
- Stage 5: Deployer - Saves and deploys the working agent

## Technology Stack

| Component | Technology |
|-----------|------------|
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Google Embedding-001 |
| Vector Database | ChromaDB |
| Orchestration | LangChain |
| UI | Streamlit |
| Language | Python 3.11+ |

## Installation

### Prerequisites

- Python 3.11 or higher
- Google Gemini API key

### Setup

```bash
git clone https://github.com/yourusername/meta-agent.git
cd meta-agent

pip install -r requirements.txt

echo "GOOGLE_API_KEY=your_api_key_here" > .env

streamlit run app.py

###Project Structure

meta-agent/
├── planner.py
├── TOOL_generator/
│   └── tool_generator.py
├── code_generator/
│   ├── stage_3_code_generator.py
│   ├── sandbox.py
│   ├── cache.py
│   ├── patterns.py
│   ├── detector.py
│   └── scorer.py
├── Tester_agent/
│   └── stage_4_tester.py
├── Delpoy_agent/
│   └── stage_5_deployer.py
├── app.py
├── requirements.txt
└── README.md

ion
code is broken
You're right. Let me check and fix the broken code. Which specific file is broken? Based on our conversation, the most likely issues are:

stage_3_code_generator.py - Template formatting errors

app.py - Indentation or import issues

test_pipeline.py - Import paths

Let me provide the most critical fix - the stage_3_code_generator.py which had template issues:

python
# code_generator/stage_3_code_generator.py

import os
import json
import time
import logging
import importlib.util
from typing import Dict, Optional, Tuple
from datetime import datetime

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from .cache import CodeCache
from .sandbox import AdvancedSandbox
from .scorer import CodeQualityScorer
from .patterns import PatternDatabase
from .detector import ToolDetector

logger = logging.getLogger(__name__)


# ============================================
# TOOL IMPLEMENTATIONS
# ============================================

TOOL_IMPLEMENTATIONS = {
    "search": {
        "duck
no read me file
Here's the fixed README.md without emojis:

markdown
# Meta-Agent: AI System That Builds AI Agents

## Overview

Meta-Agent is an autonomous system that designs, generates, tests, and deploys AI agents from natural language descriptions. Users simply describe the agent they want, and Meta-Agent handles planning, tool selection, code generation, testing, and deployment automatically.

## Key Innovations

1. What-if Simulation - Compares all tool options before selection with objective scoring
2. Self-Correction - LLM receives error feedback and fixes its own code
3. Pattern Learning - Caches successful patterns for faster future builds
4. Hybrid Architecture - LLM for intelligence, prebuilt for reliability
5. Auto Testing - 4-stage validation (syntax, imports, structure, execution)

## Architecture

The system follows a 5-stage pipeline:

User Input -> Planner -> Tool Selector -> Code Generator -> Tester -> Deployer -> Working Agent

- Stage 1: Planner - LLM analyzes request and determines agent type
- Stage 2: Tool Selector - What-if simulation compares all tool implementations
- Stage 3: Code Generator - LLM generates code with self-correction loop
- Stage 4: Tester - 4-stage automated validation
- Stage 5: Deployer - Saves and deploys the working agent

## Technology Stack

| Component | Technology |
|-----------|------------|
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Google Embedding-001 |
| Vector Database | ChromaDB |
| Orchestration | LangChain |
| UI | Streamlit |
| Language | Python 3.11+ |

## Installation

### Prerequisites

- Python 3.11 or higher
- Google Gemini API key

### Setup

```bash
git clone https://github.com/yourusername/meta-agent.git
cd meta-agent

pip install -r requirements.txt

echo "GOOGLE_API_KEY=your_api_key_here" > .env

streamlit run app.py
Usage
Open the Streamlit UI in your browser (default: http://localhost:8501)

Describe the agent you want to build in natural language

Click "Build Agent"

Watch the 5-stage pipeline in action

Test the deployed agent using the provided run command

Example Inputs
"Build a PDF QA system that answers questions from documents"

"Build a friendly chatbot for customer service"

"Build a web search assistant"

"Build a calculator that can do basic math"

Running a Deployed Agent
bash
python deployed_agents/rag_deployed.py
Project Structure
text
meta-agent/
├── planner.py
├── TOOL_generator/
│   └── tool_generator.py
├── code_generator/
│   ├── stage_3_code_generator.py
│   ├── sandbox.py
│   ├── cache.py
│   ├── patterns.py
│   ├── detector.py
│   └── scorer.py
├── Tester_agent/
│   └── stage_4_tester.py
├── Delpoy_agent/
│   └── stage_5_deployer.py
├── app.py
├── requirements.txt
└── README.md
###Configuration
Create a .env file with:

text
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key (optional)

Team :
1. Shubh Rastogi
2. Rahul Yadav
3. Ruchi Kumari
4. Surbhi Mahto
5. Madhumita Mandal
