#!/bin/bash

echo "🚀 Starting Flowing MVP..."

# Kill any old processes on ports 5000 and 5001
echo "🛑 Killing old agent processes..."
kill -9 $(lsof -t -i :5000) $(lsof -t -i :5001) 2>/dev/null

# Remove old trace logs
echo "🧹 Cleaning old trace logs..."
rm trace_log.json 2>/dev/null

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# Start agents
echo "Starting AgentA on port 5000..."
PYTHONPATH=src venv/bin/python3 examples/agent_server.py &

echo "Starting AgentX on port 5001..."
PYTHONPATH=src venv/bin/python3 examples/my_agent_server.py &

sleep 2

# Start Streamlit dashboard
echo "📊 Starting Streamlit dashboard..."
if [ -f "venv/bin/streamlit" ]; then
    venv/bin/streamlit run dashboard.py
else
    echo "⚠️ Streamlit not found in venv, please install it manually with:"
    echo "   pip install streamlit streamlit-autorefresh"
    echo "Then run ./start_flowing.sh again."
fi

echo "✅ Flowing started! Agents running and dashboard should be open."

# Start Streamlit dashboard
venv/bin/streamlit run dashboard.py &
echo "⚡ Dashboard should now be running at http://localhost:8502"
