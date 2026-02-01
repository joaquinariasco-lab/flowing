from base_agent import BaseAgent
import requests

class MyAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name)

    def on_message(self, message: str):
        print(f"[{self.name} received]: {message}")

    def on_task(self, description: str, price: float):
        print(f"[{self.name}] executing task: {description}")
        # Simula ganar el precio
        print(f"[{self.name}] earned {price}")
        return {"status": "done", "balance": price}

    # Send messages to another agents
    def send_message(self, target_url: str, message: str):
        try:
            requests.post(f"{target_url}/receive_message", json={"message": message})
            print(f"[{self.name} sent message to {target_url}]: {message}")
        except Exception as e:
            print(f"Error sending message: {e}")
