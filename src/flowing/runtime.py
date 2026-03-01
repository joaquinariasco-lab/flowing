import json


class FlowingRuntime:
    def __init__(self, mode="record", trace_path=None):
        self.mode = mode
        self.trace_data = {}
        self.pointer = 0

        if mode == "replay":
            if not trace_path:
                raise ValueError("trace_path required in replay mode")

            with open(trace_path, "r") as f:
                events = json.load(f)

            # Index by decision_id
            self.trace_data = {
                e["decision_id"]: e for e in events
            }

    def get_replay_output(self, decision_id):
        if decision_id not in self.trace_data:
            raise ValueError(f"Decision {decision_id} not found in trace")

        return self.trace_data[decision_id]["output"]
