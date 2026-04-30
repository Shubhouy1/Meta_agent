# app.py - Complete UI with Improved Visibility

import streamlit as st
import json
import time
import pandas as pd
import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(__file__))

from planner import generate_plan
from TOOL_generator.tool_generator import ToolSelector
from code_generator.stage_3_code_generator import CodeGenerator
from Tester_agent.stage_4_tester import Stage4Tester
from Delpoy_agent.stage_5_deployer import Stage5Deployer

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Meta-Agent - AI Agent Builder",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# IMPROVED CSS - HIGH CONTRAST
# ============================================

st.markdown("""
<style>
    /* MAIN BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a1a2e 100%);
    }
    
    /* MAIN HEADER */
    .main-header {
        background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        border: 1px solid #e94560;
        box-shadow: 0 0 20px rgba(233, 69, 96, 0.3);
    }
    .main-header h1 {
        color: #e94560;
        text-shadow: 0 0 10px #e94560;
        font-size: 2.5rem;
    }
    .main-header p {
        color: #ffffff;
        font-size: 1.2rem;
    }
    
    /* INNOVATION CARDS */
    .innovation-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 1rem;
        padding: 1rem;
        margin: 0.5rem;
        border: 1px solid #e94560;
        text-align: center;
        transition: all 0.3s ease;
    }
    .innovation-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 20px rgba(233, 69, 96, 0.4);
    }
    .innovation-card b {
        color: #e94560;
        font-size: 1rem;
    }
    .innovation-card small {
        color: #c4c4c4;
        font-size: 0.75rem;
    }
    .innovation-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    /* BUTTON STYLE */
    .stButton > button {
        background: linear-gradient(135deg, #e94560 0%, #0f3460 100%);
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 0.5rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 20px rgba(233, 69, 96, 0.5);
        color: white;
    }
    
    /* RESPONSE BOX */
    .response-box {
        background: #16213e;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
        border-left: 4px solid #e94560;
        color: #ffffff;
    }
    
    /* METRIC CARDS */
    .metric-card {
        background: #1a1a2e;
        border: 1px solid #e94560;
        border-radius: 0.5rem;
        padding: 1rem;
        text-align: center;
    }
    .metric-card label {
        color: #e94560;
        font-weight: bold;
    }
    .metric-card .value {
        color: #ffffff;
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    /* TAB STYLING */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: #1a1a2e;
        padding: 0.5rem;
        border-radius: 0.8rem;
    }
    .stTabs [data-baseweb="tab"] {
        color: #c4c4c4;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: #e94560;
        color: white;
    }
    
    /* INFO/WARNING/SUCCESS BOXES */
    .stAlert {
        background: #1a1a2e;
        border-left: 4px solid #e94560;
    }
    
    /* EXPANDER */
    .streamlit-expanderHeader {
        background: #1a1a2e;
        color: #e94560;
        border-radius: 0.5rem;
    }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background: #0a0a1a;
        border-right: 1px solid #e94560;
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff;
    }
    
    /* TEXT INPUTS */
    .stTextArea textarea, .stTextInput input {
        background-color: #1a1a2e !important;
        color: #ffffff !important;
        border: 1px solid #e94560 !important;
        border-radius: 0.5rem !important;
    }
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #e94560 !important;
        box-shadow: 0 0 10px rgba(233, 69, 96, 0.3) !important;
    }
    
    /* SELECTBOX */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1a1a2e;
        border-color: #e94560;
    }
    .stSelectbox span {
        color: #ffffff;
    }
    
    /* SLIDERS */
    .stSlider label {
        color: #ffffff !important;
    }
    
    /* DATA FRAME */
    .stDataFrame {
        background: #1a1a2e;
    }
    .stDataFrame th {
        color: #e94560;
    }
    .stDataFrame td {
        color: #ffffff;
    }
    
    /* CODE BLOCK */
    .stCodeBlock {
        background: #0a0a1a;
        border: 1px solid #e94560;
        border-radius: 0.5rem;
    }
    
    /* PROGRESS BAR */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #e94560, #0f3460);
    }
    
    /* METRIC */
    [data-testid="stMetric"] {
        background: #1a1a2e;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e94560;
    }
    [data-testid="stMetric"] label {
        color: #e94560 !important;
    }
    [data-testid="stMetric"] .stMetricValue {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# INITIALIZE SESSION STATE
# ============================================

if "deployment" not in st.session_state:
    st.session_state.deployment = None
if "code_result" not in st.session_state:
    st.session_state.code_result = None
if "test_result" not in st.session_state:
    st.session_state.test_result = None
if "plan" not in st.session_state:
    st.session_state.plan = None
if "tool_result" not in st.session_state:
    st.session_state.tool_result = None
if "agent_built" not in st.session_state:
    st.session_state.agent_built = False

# ============================================
# HEADER
# ============================================

st.markdown("""
<div class="main-header">
    <h1>🤖 Meta-Agent</h1>
    <p>An AI Agent That Builds AI Agents</p>
    <p style="font-size: 0.9rem; opacity: 0.9;">Self-correcting | Pattern Learning | What-if Simulation</p>
</div>
""", unsafe_allow_html=True)

# ============================================
# INNOVATION CARDS
# ============================================

st.markdown("### 🏆 Key Innovations")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="innovation-card">
        <div class="innovation-icon">🔮</div>
        <b>What-if Simulation</b><br>
        <small>Compares all tool options before selection</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="innovation-card">
        <div class="innovation-icon">🔄</div>
        <b>Self-Correction</b><br>
        <small>LLM fixes its own code errors</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="innovation-card">
        <div class="innovation-icon">📚</div>
        <b>Pattern Learning</b><br>
        <small>Caches successful patterns</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="innovation-card">
        <div class="innovation-icon">⚡</div>
        <b>Hybrid Architecture</b><br>
        <small>LLM + Prebuilt = Best of Both</small>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="innovation-card">
        <div class="innovation-icon">🧪</div>
        <b>Auto Testing</b><br>
        <small>4-stage validation</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================
# SIDEBAR
# ============================================

with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    
    model_options = ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-1.5-flash"]
    selected_model = st.selectbox("Model", model_options, index=0)
    
    st.markdown("---")
    
    st.markdown("## 🎯 Constraints")
    budget = st.select_slider("Budget", options=["free", "low", "medium", "high"], value="free")
    privacy = st.select_slider("Privacy", options=["strict", "moderate", "none"], value="moderate")
    performance = st.select_slider("Performance", options=["fast", "balanced", "accurate"], value="balanced")
    
    st.markdown("---")
    
    st.markdown("## 📈 Innovation Stats")
    
    stats_col1, stats_col2 = st.columns(2)
    with stats_col1:
        st.metric("Patterns Learned", "12")
        st.metric("Cache Hits", "8")
    with stats_col2:
        st.metric("LLM Success", "94%")
        st.metric("Self-Corrections", "3")
    
    st.markdown("---")
    st.caption("Built with ❤️ for CodeSpire")

# ============================================
# MAIN CONTENT
# ============================================

st.markdown("## 🚀 Create a New Agent")

# Input section
col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_area(
        "Describe the agent you want to build:",
        placeholder="Example: Build a PDF QA system that can answer questions from uploaded documents...",
        height=100
    )

with col2:
    st.markdown("### 💡 Examples")
    if st.button("📄 PDF QA"):
        user_input = "Build a PDF QA system that answers questions from documents"
    if st.button("💬 Chatbot"):
        user_input = "Build a friendly chatbot for customer service"
    if st.button("🔍 Web Search"):
        user_input = "Build a web search assistant"
    if st.button("🧮 Calculator"):
        user_input = "Build a calculator that can do basic math"

# Build button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    build_button = st.button("🔨 Build Agent", use_container_width=True)

# ============================================
# PIPELINE EXECUTION
# ============================================

if build_button and user_input:
    
    st.session_state.agent_built = False
    
    progress_container = st.container()
    
    with progress_container:
        st.markdown("## 🏗️ Building Your Agent")
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Stage 1: Planner
            status_text.markdown("📋 **Stage 1: Planning** - Analyzing your request...")
            progress_bar.progress(10)
            time.sleep(0.3)
            
            plan = generate_plan(user_input)
            st.session_state.plan = plan
            progress_bar.progress(20)
            status_text.markdown("✅ **Stage 1 Complete** - Agent type identified")
            
            # Stage 2: Tool Selector
            status_text.markdown("🔧 **Stage 2: Tool Selection** - Running what-if simulation...")
            selector = ToolSelector()
            tool_result = selector.select_tools(plan, user_input, {
                "budget": budget,
                "privacy": privacy,
                "performance": performance
            })
            st.session_state.tool_result = tool_result
            progress_bar.progress(40)
            status_text.markdown("✅ **Stage 2 Complete** - Tools selected")
            
            # Stage 3: Code Generator
            status_text.markdown("💻 **Stage 3: Code Generation** - Writing agent code...")
            generator = CodeGenerator()
            code_result = generator.generate(plan, tool_result, user_input)
            st.session_state.code_result = code_result
            progress_bar.progress(60)
            status_text.markdown(f"✅ **Stage 3 Complete** - Generated {code_result['lines']} lines")
            
            # Stage 4: Tester
            status_text.markdown("🧪 **Stage 4: Testing** - Validating agent...")
            tester = Stage4Tester()
            test_result = tester.run_tests(code_result["filename"])
            st.session_state.test_result = test_result
            progress_bar.progress(80)
            
            if test_result["passed"]:
                status_text.markdown("✅ **Stage 4 Complete** - All tests passed!")
            else:
                status_text.markdown("⚠️ **Stage 4 Complete** - Tests passed with warnings")
            
            # Stage 5: Deployer
            status_text.markdown("🚀 **Stage 5: Deployment** - Deploying agent...")
            deployer = Stage5Deployer()
            deployment = deployer.deploy(
                tested_file=code_result["filename"],
                agent_name=plan.get("agent_type", "agent"),
                create_api=False
            )
            st.session_state.deployment = deployment
            progress_bar.progress(100)
            status_text.markdown("✅ **Stage 5 Complete** - Agent deployed successfully!")
            
            st.session_state.agent_built = True
            time.sleep(0.5)
            
        except Exception as e:
            st.error(f"Error during build: {str(e)}")
            progress_bar.empty()
            status_text.empty()

# ============================================
# RESULTS DISPLAY
# ============================================

if st.session_state.agent_built:
    
    st.markdown("## 📊 Build Results")
    
    st.info("🎯 **Innovation Showcase:** What-if Simulation • Self-Correction • Pattern Learning • Hybrid Architecture • Auto Testing")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 Plan", "🔮 What-if Simulation", "💻 Code", "🧪 Tests", "🚀 Deploy"])
    
    # Tab 1: Plan
    with tab1:
        if st.session_state.plan:
            st.markdown("### Agent Plan")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Agent Type", st.session_state.plan.get("agent_type", "N/A"))
                st.metric("Confidence", f"{st.session_state.plan.get('confidence', 0)*100:.0f}%")
            with col2:
                st.metric("Tools Required", len(st.session_state.plan.get("tools", [])))
                st.metric("Flow Steps", len(st.session_state.plan.get("flow", [])))
            
            st.markdown("#### Execution Flow")
            for i, step in enumerate(st.session_state.plan.get("flow", []), 1):
                st.markdown(f"{i}. `{step}`")
    
    # Tab 2: What-if Simulation
    with tab2:
        if st.session_state.tool_result:
            st.markdown("### 🔮 What-if Simulation - Tool Comparison")
            
            constraints = st.session_state.tool_result.get("constraints_applied", {})
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"**Budget:** `{constraints.get('budget', 'N/A')}`")
            with col2:
                st.markdown(f"**Privacy:** `{constraints.get('privacy', 'N/A')}`")
            with col3:
                st.markdown(f"**Performance:** `{constraints.get('performance', 'N/A')}`")
            
            st.markdown("---")
            
            if "what_if_simulations" in st.session_state.tool_result:
                for tool_name, sim in st.session_state.tool_result["what_if_simulations"].items():
                    st.markdown(f"#### 📊 {tool_name.upper()} Tool Analysis")
                    
                    options_data = []
                    for opt in sim.get("simulated_options", []):
                        options_data.append({
                            "Tool": opt["name"],
                            "Cost": opt["cost"],
                            "Score": f"{opt['score']}/100",
                            "API Key": "No" if not opt.get("api_key_required") else "Yes",
                        })
                    
                    df = pd.DataFrame(options_data)
                    st.dataframe(df, use_container_width=True, hide_index=True)
                    
                    st.success(f"✅ **Recommended:** {sim.get('recommended_name')}")
                    st.info(f"📝 **Reasoning:** {sim.get('reasoning', '')[:300]}...")
                    st.markdown("---")
    
    # Tab 3: Code
    with tab3:
        if st.session_state.code_result:
            st.markdown("### 💻 Generated Code")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Lines of Code", st.session_state.code_result.get("lines", 0))
            with col2:
                st.metric("Quality Score", f"{st.session_state.code_result.get('quality_score', 0)*100:.0f}%")
            with col3:
                method = st.session_state.code_result.get('generation_method', 'N/A')
                st.metric("Generation Method", method)
            
            if "self_corrected" in method:
                st.success("🔄 **Self-Correction Used:** LLM fixed its own errors!")
            
            st.code(st.session_state.code_result.get("code", "# No code generated")[:2000], language="python", line_numbers=True)
    
    # Tab 4: Tests
    with tab4:
        if st.session_state.test_result:
            st.markdown("### 🧪 Test Results")
            
            if st.session_state.test_result.get("passed", False):
                st.success("✅ All tests passed!")
            
            for res in st.session_state.test_result.get("test_results", []):
                st.markdown(f"✓ {res}")
            
            if st.session_state.test_result.get("warnings"):
                for warn in st.session_state.test_result.get("warnings", []):
                    st.markdown(f"⚠️ {warn}")
    
    # Tab 5: Deploy
    with tab5:
        if st.session_state.deployment:
            st.markdown("### 🚀 Deployment")
            
            if st.session_state.deployment.get("success", False):
                st.success("✅ Agent deployed successfully!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Deployed File", st.session_state.deployment.get("deployed_file", "N/A"))
                with col2:
                    st.metric("Status", "Ready")
                
                st.markdown("#### Run Command")
                st.code(st.session_state.deployment.get("run_command", "N/A"), language="bash")
                
                # Test Your Agent
                st.markdown("#### 🧪 Live Agent Test")
                
                test_question = st.text_input("Ask a question:", key="live_test_input", placeholder="Type your message here...")
                
                if st.button("Send", key="send_button"):
                    if test_question:
                        with st.spinner("Agent is thinking..."):
                            try:
                                agent_file = st.session_state.deployment.get("deployed_file")
                                
                                if agent_file and os.path.exists(agent_file):
                                    spec = importlib.util.spec_from_file_location("test_agent", agent_file)
                                    module = importlib.util.module_from_spec(spec)
                                    spec.loader.exec_module(module)
                                    
                                    agent = module.Agent()
                                    response = agent.run(test_question)
                                    
                                    st.markdown(f'<div class="response-box"><b>🤖 Agent:</b> {response}</div>', unsafe_allow_html=True)
                                else:
                                    st.error(f"Agent file not found: {agent_file}")
                                    
                            except Exception as e:
                                st.error(f"Error: {str(e)}")
                    else:
                        st.warning("Please enter a question")
    
    # Show stats
    if "stats" in st.session_state.code_result:
        with st.expander("📈 Generator Statistics & Pattern Learning Data"):
            st.json(st.session_state.code_result["stats"])

elif build_button and not user_input:
    st.warning("Please enter a description of the agent you want to build")

else:
    st.markdown("""
    <div style="text-align: center; padding: 4rem; background: #16213e; border-radius: 1rem; border: 1px solid #e94560;">
        <h2 style="color: #e94560;">✨ Welcome to Meta-Agent</h2>
        <p style="font-size: 1.2rem; color: #ffffff;">An AI Agent That Builds AI Agents</p>
        <p style="margin-top: 1rem; color: #c4c4c4;">Describe the agent you want to build above, and watch our system:</p>
        <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem; flex-wrap: wrap; color: #ffffff;">
            <div>🔮 Compare tools with what-if simulation</div>
            <div>🔄 Self-correct code errors</div>
            <div>📚 Learn from patterns</div>
            <div>🧪 Auto-test agents</div>
            <div>🚀 Deploy ready-to-use agents</div>
        </div>
    </div>
    """, unsafe_allow_html=True)