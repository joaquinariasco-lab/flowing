#!/bin/bash

source venv/bin/activate
cd examples

echo "Starting AgentA..."
python3 agent_server.py &

echo "Starting AgentX..."
python3 my_agent_server.py &
