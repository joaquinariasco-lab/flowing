#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Kill old agents if they exist
kill -9 $(lsof -ti:5000) 2>/dev/null
kill -9 $(lsof -ti:5001) 2>/dev/null

# Clean trace log
rm -f trace_log.json

# Start agents in background
python3 langchain/my_agent_server.py &   # adjust filename if different
python3 langchain/agent_server.py &      # adjust filename if different

# Wait a few seconds for agents to start
sleep 3

# Start Streamlit dashboard in background
streamlit run dashboard.py &

# Wait a few seconds for Streamlit server to start
sleep 3

# Automatically open default browser to the dashboard
python3 -m webbrowser http://localhost:8501

echo "Flowing started! Agents running and dashboard opened in browser."
