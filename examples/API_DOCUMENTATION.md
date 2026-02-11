# Flowing API Documentation

Complete reference for all HTTP endpoints in the Flowing agent interoperability framework.

## Base URLs

Agent A: http://localhost:5000
Agent B: http://localhost:5001
Agent C: http://localhost:5002
WebSocket Agent: http://localhost:5002

## Agent Endpoints

### 1. Receive Message

Send a text message to an agent.

Endpoint: POST /receive_message
Content-Type: application/json

Request Body:
{
  "message": "string - message content",
  "sender": "string - name of sending agent (optional)"
}

Response:
{
  "status": "ok"
}

Status Codes:
- 200 OK - Message received successfully
- 400 Bad Request - Invalid message format
- 500 Internal Server Error - Server error

Example:
curl -X POST http://localhost:5000/receive_message \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello Agent", "sender": "AgentX"}'

---

### 2. Run Task

Send a task to an agent for execution.

Endpoint: POST /run_task
Content-Type: application/json

Request Body:
{
  "description": "string - task description",
  "price": "float - task compensation",
  "sender": "string - name of sending agent (optional)"
}

Response:
{
  "status": "done",
  "balance": "float - agent balance after task completion"
}

Status Codes:
- 200 OK - Task executed successfully
- 400 Bad Request - Invalid task format
- 500 Internal Server Error - Task execution failed

Example:
curl -X POST http://localhost:5000/run_task \
  -H "Content-Type: application/json" \
  -d '{"description": "Analyze data", "price": 50.5, "sender": "Controller"}'

---

### 3. Get Agent Identity

Retrieve agent metadata and capabilities.

Endpoint: GET /identity

Response:
{
  "name": "string - agent name",
  "framework": "string - underlying framework",
  "capabilities": ["array", "of", "capabilities"],
  "accepts_tasks": "boolean - whether agent accepts tasks",
  "pricing_model": "string - pricing model type",
  "version": "string - agent version"
}

Status Codes:
- 200 OK - Identity returned successfully
- 500 Internal Server Error - Server error

Example:
curl -X GET http://localhost:5000/identity

Response:
{
  "name": "AgentA",
  "framework": "custom",
  "capabilities": ["example-task"],
  "accepts_tasks": true,
  "pricing_model": "fixed",
  "version": "0.1"
}

---

## WebSocket Agent Endpoints

All standard endpoints (receive_message, run_task, identity) plus:

### 4. Get Message Log

Retrieve all received messages for WebSocket agent.

Endpoint: GET /message_log

Response:
{
  "logs": [
    {
      "timestamp": "ISO8601 timestamp",
      "sender": "string - sending agent",
      "message": "string - message content"
    }
  ]
}

Example:
curl -X GET http://localhost:5002/message_log

---

## AutonomousController Endpoints

(If exposed as REST service)

### 5. Run Cycle

Execute one cycle of task generation, assignment, execution, and evaluation.

Endpoint: POST /run_cycle

Request Body (optional):
{
  "num_tasks": "integer - number of tasks to generate (default: 5)"
}

Response:
{
  "cycle": "integer - cycle number",
  "evaluation": {
    "total_tasks": "integer",
    "successful": "integer",
    "failed": "integer",
    "success_rate": "float - percentage"
  },
  "balances": {
    "AgentA": "float - current balance",
    "AgentB": "float - current balance"
  },
  "timestamp": "ISO8601 timestamp"
}

---

### 6. Get Statistics

Retrieve overall controller statistics.

Endpoint: GET /statistics

Response:
{
  "cycles_completed": "integer",
  "total_tasks_generated": "integer",
  "total_assignments": "integer",
  "successful_assignments": "integer",
  "success_rate": "float - percentage",
  "agent_balances": {
    "AgentA": "float",
    "AgentB": "float"
  },
  "timestamp": "ISO8601 timestamp"
}

---

### 7. Save Report

Generate and save a JSON report of all activities.

Endpoint: POST /save_report

Request Body (optional):
{
  "filename": "string - output filename (default: controller_report.json)"
}

Response:
{
  "status": "ok",
  "filename": "string - generated report filename"
}

---

## Communication Client Usage

### Python Client Library

Using CommunicationClient for safe inter-agent communication:

from communication_utils import CommunicationClient

client = CommunicationClient(max_retries=3, timeout=5, backoff_factor=2)

Send Message:
result = client.send_message(
  target_url="http://localhost:5000",
  message="Hello from Agent",
  sender_name="AgentB"
)

Send Task:
result = client.send_task(
  target_url="http://localhost:5000",
  description="Process data",
  price=25.0,
  sender_name="AutonomousController"
)

Health Check:
is_online = client.health_check("http://localhost:5000")

---

## Error Responses

All endpoints may return error responses with the following format:

{
  "error": "string - error description",
  "status": "failed"
}

Common Error Codes:

400 Bad Request
- Missing required fields
- Invalid data format
- Invalid JSON in request body

401 Unauthorized
- Missing or invalid authentication credentials (if enabled)

403 Forbidden
- Agent does not accept tasks
- Permission denied

404 Not Found
- Endpoint does not exist
- Agent not found

500 Internal Server Error
- Task execution failure
- Database error
- Unexpected server error

503 Service Unavailable
- Agent is offline
- Database connection lost

---

## Request Authentication (Optional)

If basic authentication is enabled, all requests must include:

Authorization: Basic base64(username:password)

Example:
curl -X POST http://localhost:5000/receive_message \
  -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{"message": "Test message"}'

---

## Rate Limiting

No rate limiting is currently implemented. Implement in production.

---

## Timeouts

Default request timeout: 5 seconds
Health check timeout: 2 seconds
Connection timeout: 3 seconds

Customize via CommunicationClient initialization.

---

## Versioning

Current API Version: 1.0
Compatible with Flowing v0.1+

---

## Examples

### Example 1: Agent Discovery

Discover all available agents:

import json
import requests

with open("agents.json") as f:
    agents = json.load(f)

for name, url in agents.items():
    try:
        response = requests.get(f"{url}/identity", timeout=2)
        identity = response.json()
        print(f"Found: {name} - {identity['framework']}")
    except Exception as e:
        print(f"Agent {name} is unreachable")

---

### Example 2: Send Task Chain

Send a task through multiple agents:

from communication_utils import CommunicationClient

client = CommunicationClient()

agents = [
  "http://localhost:5000",
  "http://localhost:5001",
  "http://localhost:5002"
]

for agent_url in agents:
    result = client.send_task(
        target_url=agent_url,
        description="Process workflow step",
        price=10.0,
        sender_name="Orchestrator"
    )
    
    if result.get("status") == "failed":
        print(f"Failed at {agent_url}: {result.get('error')}")
        break

---

### Example 3: Run Autonomous Cycle

from autonomous_controller import AutonomousController

agents = {
    "AgentA": "http://localhost:5000",
    "AgentB": "http://localhost:5001"
}

controller = AutonomousController(agents, initial_balance=100.0)
controller.run_multiple_cycles(num_cycles=3, num_tasks=5, interval=2.0)

stats = controller.get_statistics()
print(f"Success Rate: {stats['success_rate']}%")
controller.save_report()

---

## Testing Endpoints

Test all endpoints using provided curl commands or Postman collection.

For quick testing, use the discover_agents.py script:

python discover_agents.py

This will connect to all agents defined in agents.json and display their identity information.

---

## Support and Issues

For bugs or feature requests, open an issue on GitHub.

Repository: https://github.com/joaquinariasco-lab/flowing
