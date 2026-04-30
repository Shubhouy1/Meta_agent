# code_generator/templates.py

from langchain_core.prompts import PromptTemplate

# ============================================
# TOOL IMPLEMENTATIONS
# ============================================

TOOL_IMPLEMENTATIONS = {
    "search": {
        "duckduckgo": '''
def search_tool(query: str) -> str:
    return f"[SEARCH RESULT] {query}"
'''
    },

    "calculator": {
        "safe_eval": '''
def calculate_tool(expr: str) -> str:
    try:
        return str(eval(expr))
    except:
        return f"Calculation error: {expr}"
'''
    },

    "retriever": {
        "chromadb": '''
def retriever_tool(query: str) -> str:
    return f"[RETRIEVED DATA] {query}"
'''
    },

    "memory": {
        "buffer": '''
class MemoryTool:
    def __init__(self):
        self.history = []

    def store(self, user_input, response):
        self.history.append((user_input, response))

    def get_context(self):
        return str(self.history)
'''
    }
}

# ============================================
# AGENT TEMPLATES
# ============================================

AGENT_TEMPLATES = {

    "chatbot": '''"""
CHATBOT AGENT
Generated: {timestamp}
Request: {user_request}
Method: {method}
"""

class Agent:
    def __init__(self):
        self.history = []

    def run(self, user_input: str) -> str:
        if "hello" in user_input.lower():
            return "Hello!"
        return f"You said: {user_input}"


if __name__ == "__main__":
    agent = Agent()
    while True:
        user = input("You: ")
        if user == "exit":
            break
        print(agent.run(user))
''',

    "rag": '''"""
RAG AGENT
Generated: {timestamp}
Request: {user_request}
Method: {method}
"""

{tool_code}

class Agent:
    def __init__(self):
        self.retriever = retriever_tool

    def run(self, user_input: str) -> str:
        data = self.retriever(user_input)
        return f"Answer based on: {data}"


if __name__ == "__main__":
    agent = Agent()
    while True:
        user = input("Q: ")
        if user == "exit":
            break
        print(agent.run(user))
''',

    "tool_agent": '''"""
TOOL AGENT
Generated: {timestamp}
Request: {user_request}
Method: {method}
"""

{tool_code}

class Agent:
    def __init__(self):
        self.tools = {{ {tool_registry} }}

    def run(self, user_input: str) -> str:
        if "+" in user_input:
            return self.tools.get("calculator", lambda x: "No calc")(user_input)

        if "search" in user_input.lower():
            return self.tools.get("search", lambda x: "No search")(user_input)

        return "No tool matched"


if __name__ == "__main__":
    agent = Agent()
    while True:
        user = input("You: ")
        if user == "exit":
            break
        print(agent.run(user))
'''
}

# ============================================
# LLM PROMPT (FULLY FIXED)
# ============================================

CODE_GEN_PROMPT = PromptTemplate(
    input_variables=["agent_type", "selected_tools", "user_request", "tool_hint"],
    template="""
You are an expert Python developer.

Generate a simple, runnable Python agent.

AGENT TYPE: {agent_type}
TOOLS: {selected_tools}
USER REQUEST: {user_request}

STRICT RULES:
- No os, subprocess
- Must have class Agent
- Must have run(user_input: str)

OUTPUT ONLY CODE:

```python
class Agent:
    def __init__(self):
        pass

    def run(self, user_input: str) -> str:
        try:
            return "Processed: " + user_input
        except Exception as e:
            return "Error: " + str(e)

if __name__ == "__main__":
    agent = Agent()
    while True:
        user = input("You: ")
        if user.lower() == "exit":
            break
        print("Agent:", agent.run(user))

        """
)