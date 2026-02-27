import json
import time
import uuid
from pathlib import Path

TRACE_DIR = Path("traces")
TRACE_DIR.mkdir(exist_ok=True)

class Tracer:
    def __init__(self, trace_id=None):
        self.trace_id = trace_id or str(uuid.uuid4())
        self.file_path = TRACE_DIR / f"{self.trace_id}.json"
        self.events = []

    def log(self, agent, event_type, payload=None, parent_span=None):
        event = {
            "trace_id": self.trace_id,
            "span_id": str(uuid.uuid4()),
            "parent_span": parent_span,
            "agent": agent,
            "event_type": event_type,
            "timestamp": time.time(),
            "payload": payload
        }
        self.events.append(event)

 def flush(self):
    existing_events = []
    if self.file_path.exists():
        try:
            with open(self.file_path, "r") as f:
                existing_events = json.load(f)
        except Exception:
            existing_events = []
    combined_events = existing_events + self.events
    with open(self.file_path, "w") as f:
        json.dump(combined_events, f, indent=2)
    self.events = []  # clean the buffer before write
