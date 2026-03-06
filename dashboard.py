import streamlit as st
import time
import random
import pandas as pd

st.set_page_config(
    page_title="Flowing – Agent Observability",
    layout="wide"
)

st.title("⚡ Flowing – AI Agent Observability")

st.markdown(
"""
Real-time tracing for AI agents.

Flowing captures:

- Chain execution
- Tool calls
- Latency
- Failures
- Agent reasoning paths
"""
)

st.divider()

# simulate trace data

runs = [
    {"step": "Agent start", "latency": round(random.uniform(0.01,0.05),3), "status": "ok"},
    {"step": "Tool: search", "latency": round(random.uniform(0.05,0.2),3), "status": "ok"},
    {"step": "Tool: calculator", "latency": round(random.uniform(0.01,0.08),3), "status": "ok"},
    {"step": "LLM reasoning", "latency": round(random.uniform(0.2,0.5),3), "status": "ok"},
    {"step": "Final answer", "latency": round(random.uniform(0.01,0.03),3), "status": "ok"},
]

df = pd.DataFrame(runs)

col1, col2 = st.columns(2)

with col1:

    st.subheader("Execution Trace")

    for run in runs:
        st.write(
            f"**{run['step']}** — {run['latency']}s — {run['status']}"
        )
        time.sleep(0.1)

with col2:

    st.subheader("Latency Table")

    st.dataframe(df)

st.divider()

st.subheader("Execution Graph")

st.graphviz_chart(
"""
digraph {
Agent -> SearchTool
SearchTool -> LLM
LLM -> Calculator
Calculator -> LLM
LLM -> Answer
}
"""
)

st.divider()

st.success("Flowing tracing active")

st.caption("Observe every step of your AI agent.")
