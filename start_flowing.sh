#!/bin/bash

echo "Starting Flowing MVP..."

# Activate virtual environment
source venv/bin/activate

# Start AgentA in background
echo "Starting AgentA on port 5000..."
PYTHONPATH=src venv/bin/python3 examples/agent_server.py &

# Start AgentX in background
echo "Starting AgentX on port 5001..."
PYTHONPATH=src venv/bin/python3 examples/my_agent_server.py &

# Wait a moment for servers to be ready
sleep 2

# Start Streamlit dashboard in background
echo "Starting Streamlit dashboard..."
venv/bin/streamlit run dashboard.py &

# Try to automatically open the browser (Linux/Mac/Windows)
if command -v xdg-open >/dev/null; then
    xdg-open http://localhost:8502
elif command -v open >/dev/null; then
    open http://localhost:8502
elif command -v start >/dev/null; then
    start http://localhost:8502
else
    echo "⚠️ Could not auto-open browser. Open manually: http://localhost:8502"
fi

echo "Flowing started! Agents running and dashboard should be open."
