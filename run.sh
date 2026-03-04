#!/bin/bash

echo "Starting AgentA on port 5000..."
PYTHONPATH=src venv/bin/python3 examples/agent_server.py &

echo "Starting AgentX on port 5001..."
PYTHONPATH=src venv/bin/python3 examples/my_agent_server.py &

sleep 2

echo "Sending test message..."
curl -X POST http://localhost:5001/message \
  -H "Content-Type: application/json" \
  -d '{"message":"hello"}'

echo "Demo complete."
