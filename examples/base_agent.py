from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def on_message(self, message: str):
        pass

    @abstractmethod
    def on_task(self, description: str, price: float):
        pass
