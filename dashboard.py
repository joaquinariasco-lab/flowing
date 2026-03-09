import json
import streamlit as st
import time

st.title("Flowing Agent Activity")

events = []

try:
    with open("trace_log.json") as f:
        for line in f:
            events.append(json.loads(line))
except:
    pass

for e in events:
    st.write(
        e["agent"],
        e["step"],
        e["details"],
        time.ctime(e["timestamp"])
    )
