#!/bin/bash

source venv/bin/activate
cd examples

echo "Starting AgentA on port 5000..."
python3 agent_server.py &

echo "Starting AgentX on port 5001..."
python3 my_agent_server.py &

echo "Waiting for servers to start..."
sleep 3

echo "Sending test message..."
curl -X POST http://localhost:5001/receive_message \
-H "Content-Type: application/json" \
-d '{"message": "Hello from AgentA"}'

echo ""
echo "✅ Demo complete. Agents are running."

wait
