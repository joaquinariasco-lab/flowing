# src/flowing/decision/span.py

from contextlib import ContextDecorator
from typing import Optional
from .event import DecisionEvent


class DecisionSpan(ContextDecorator):
    def __init__(self, tracer, agent_id: str, parent_id: Optional[str] = None):
        self.tracer = tracer
        self.agent_id = agent_id
        self.parent_id = parent_id
        self.event = None

    def start(self):
        self.event = DecisionEvent(
            agent_id=self.agent_id,
            prompt="",
            model="",
            temperature=0.0,
            output="",
            parent_id=self.parent_id
        )
        return self

    def record_prompt(self, prompt: str):
        self.event.prompt = prompt

    def record_model(self, model: str, temperature: float):
        self.event.model = model
        self.event.temperature = temperature

    def record_output(self, output: str):
        self.event.output = output

    def end(self):
        self.tracer.record(self.event)

    def __enter__(self):
        return self.start()

    def __exit__(self, *exc):
        self.end()
