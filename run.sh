#!/bin/bash

source venv/bin/activate
cd examples

echo "Starting AgentA on port 5000..."
python3 agent_server.py &

echo "Starting AgentX on port 5001..."
python3 my_agent_server.py &

echo "✅ Agents running on ports 5000 and 5001."
wait
