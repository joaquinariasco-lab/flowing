import requests
from example_agent import ExampleAgent

def send_message_http(self, target_url, message):
    try:
        requests.post(f"{target_url}/receive_message", json={"message": message})
        print(f"[{self.name} sending to {target_url}]: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

class EconomicAgent(ExampleAgent):
    def __init__(self, name, balance=10):
        super().__init__(name)
        self.balance = balance

    def can_accept_task(self, price):
        return self.balance >= 0

    def earn(self, amount):
        self.balance += amount

    def lose(self, amount):
        self.balance -= amount
