from flask import Flask, request
from economic_agent import EconomicAgent

# Agent setting
agent_name = "AgentA"  
agent = EconomicAgent(agent_name, balance=10)

app = Flask(__name__)

# Endpoint to receive messages from another agents
@app.route("/receive_message", methods=["POST"])
def receive_message():
    data = request.json
    message = data.get("message")
    print(f"[{agent.name} received]: {message}")
    return {"status": "ok"}

# Endpoint to receive economic tasks
@app.route("/run_task", methods=["POST"])
def run_task_endpoint():
    data = request.json
    task_description = data.get("description")
    task_price = data.get("price")
    
    agent.earn(task_price)
    
    print(f"[{agent.name}] received task: {task_description} and earned {task_price}")
    print(f"[{agent.name}] new balance: {agent.balance}")
    
    return {"status": "done", "balance": agent.balance}

if __name__ == "__main__":
    app.run(port=5000)  # cada dev elige un puerto diferente
