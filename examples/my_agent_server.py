from flask import Flask, request
from my_agent import MyAgent

agent = MyAgent("AgentX")  # Cambiar nombre si otro dev clona
app = Flask(__name__)

@app.route("/receive_message", methods=["POST"])
def receive_message():
    data = request.json
    agent.on_message(data.get("message"))
    return {"status": "ok"}

@app.route("/run_task", methods=["POST"])
def run_task():
    data = request.json
    return agent.on_task(data.get("description"), data.get("price"))

if __name__ == "__main__":
    app.run(port=5001)
