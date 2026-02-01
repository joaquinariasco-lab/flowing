from flask import Flask, request
from base_agent import BaseAgent

# Example reference implementation
class SimpleAgent(BaseAgent):
    def __init__(self, name, balance=0):
        super().__init__(name)
        self.balance = balance

    def on_message(self, message: str):
        print(f"[{self.name} received]: {message}")

    def on_task(self, description: str, price: float):
        self.balance += price
        print(f"[{self.name}] completed task: {description}")
        print(f"[{self.name}] earned {price}, balance = {self.balance}")
        return {"status": "done", "balance": self.balance}


agent = SimpleAgent("AgentA", balance=10)
app = Flask(__name__)

@app.route("/receive_message", methods=["POST"])
def receive_message():
    data = request.json
    agent.on_message(data.get("message"))
    return {"status": "ok"}

@app.route("/run_task", methods=["POST"])
def run_task():
    data = request.json
    return agent.on_task(
        data.get("description"),
        data.get("price")
    )

if __name__ == "__main__":
    app.run(port=5000)
