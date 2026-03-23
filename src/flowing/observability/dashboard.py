import streamlit as st
import json
import time
from datetime import datetime
from random import choice, randint

st.title("Flowing Agent Activity")

# Autorefresh every 2 seconds
try:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=2000, key="flowing_refresh")
except:
    st.warning("Install streamlit_autorefresh to enable auto-refresh")

# Try loading trace_log.json
events = []
try:
    with open("trace_log.json") as f:
        for line in f:
            events.append(json.loads(line))
except FileNotFoundError:
    st.info("No trace log found — generating demo events...")
    agents = ["Agent_A", "Agent_B"]
    steps = ["Step 1", "Step 2", "Step 3"]
    for i in range(10):
        events.append({
            "agent": choice(agents),
            "step": choice(steps),
            "details": f"Demo output {i+1}",
            "timestamp": time.time() - randint(0, 600)
        })

# Display events in a table
if events:
    for e in events:
        st.write(
            e["agent"],
            e["step"],
            e["details"],
            datetime.fromtimestamp(e["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        )
