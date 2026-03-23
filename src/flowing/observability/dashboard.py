import streamlit as st
from streamlit_autorefresh import st_autorefresh
import json
import time
import pandas as pd
import plotly.express as px

# ----------------------------
# Auto-refresh every 2 seconds
# ----------------------------
st_autorefresh(interval=2000, key="flowing_refresh")

# ----------------------------
# Page Title & Sidebar
# ----------------------------
st.set_page_config(page_title="🌊 Flowing-OS Dashboard", layout="wide")
st.title("🌊 Flowing-OS Dashboard")

st.sidebar.header("Controls")
selected_agent = st.sidebar.selectbox("Select agent", ["All", "Agent_A", "Agent_B"])
refresh_logs = st.sidebar.button("Refresh Logs")

# ----------------------------
# Load Events
# ----------------------------
events = []

try:
    with open("trace_log.json") as f:
        for line in f:
            events.append(json.loads(line))
except FileNotFoundError:
    st.warning("No trace log found yet. Agents might not have produced any output.")

# Filter by selected agent
if selected_agent != "All":
    events = [e for e in events if e["agent_id"] == selected_agent]

# ----------------------------
# Display Agent Activity
# ----------------------------
st.subheader("Agent Activity")
if events:
    for e in events:
        with st.expander(f"{e['agent_id']} | {e['step']}"):
            st.write("**Input:**", e.get("input", ""))
            st.write("**Output:**", e.get("output", ""))
            st.write("**Details:**", e.get("details", ""))
            st.write("**Time:**", time.ctime(e.get("timestamp", 0)))
else:
    st.info("No events to display.")

# ----------------------------
# Display Metrics
# ----------------------------
if events:
    df = pd.DataFrame(events)
    
    # Steps per Agent
    st.subheader("Steps per Agent")
    step_counts = df.groupby("agent_id")["step"].count().reset_index()
    fig1 = px.bar(step_counts, x="agent_id", y="step", title="Steps executed by each agent")
    st.plotly_chart(fig1, use_container_width=True)

    # Timeline of Events
    st.subheader("Event Timeline")
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s')
    fig2 = px.line(df, x="timestamp", y="step", color="agent_id", markers=True, title="Event Timeline by Agent")
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Footer / Dev Info
# ----------------------------
st.sidebar.markdown("---")
st.sidebar.info("Flowing-OS Dashboard for live demo and developer monitoring.")
