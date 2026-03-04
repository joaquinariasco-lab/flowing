from typing import List, Optional
from dataclasses import asdict
import json

from flowing.decision.event import DecisionEvent
from flowing.decision.span import DecisionSpan


class Tracer:
    def __init__(self):
        # Initialize the events list
        self.events: List[DecisionEvent] = []

    def decision_span(self, agent_id: str, parent_id=None):
        return DecisionSpan(self, agent_id, parent_id)

    def record(self, event: DecisionEvent):
        self.events.append(event)

    # Convenience wrapper for demo compatibility
    def log(self, agent_id: str, event_type: str, metadata: Optional[dict] = None):
        event = DecisionEvent(
            agent_id=agent_id,
            prompt=event_type,
            model="none",
            temperature=0.0,
            output=str(metadata or {}),
            tool_calls=[],
            parent_id=None
        )
        self.record(event)

    def flush(self):
        # No-op for demo compatibility
        pass

    def export(self):
        return [asdict(event) for event in self.events]

    def export_json(self, path="trace.json"):
        with open(path, "w") as f:
            json.dump(self.export(), f, indent=2)
