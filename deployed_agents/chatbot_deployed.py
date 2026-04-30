"""
CHATBOT AGENT (Template Fallback)
Generated: 2026-04-30T21:11:42.241348
Request: Build a chabot
Method: template_fallback
"""

class Agent:
    def __init__(self):
        self.history = []

    def run(self, inp: str) -> str:
        low = inp.lower()
        if any(g in low for g in ['hi', 'hello', 'hey']):
            resp = "Hello! How can I help you today?"
        elif any(b in low for b in ['bye', 'exit', 'quit']):
            resp = "Goodbye! Have a great day!"
        else:
            resp = f"You said: {inp}\n\nHow can I assist you?"

        self.history.append((inp, resp))
        return resp

if __name__ == "__main__":
    agent = Agent()
    print("Chatbot Ready. Type 'exit' to quit.")
    while True:
        u = input("\nYou: ")
        if u.lower() == "exit":
            print("Goodbye!")
            break
        print(f"Bot: {agent.run(u)}")
