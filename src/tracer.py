import json
import time

def trace_event(agent, step, details):
    event = {
        "agent": agent,
        "step": step,
        "details": details,
        "timestamp": time.time()
    }

    with open("trace_log.json", "a") as f:
        f.write(json.dumps(event) + "\n")
