from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from base_agent import BaseAgent
from datetime import datetime
import json

class WebSocketAgent(BaseAgent):
    """
    Agent with bidirectional WebSocket communication capabilities
    Allows real-time message and task broadcasting
    """
    
    def __init__(self, name, socketio=None):
        super().__init__(name)
        self.socketio = socketio
        self.connected_agents = {}
        self.message_log = []
    
    def on_message(self, message: str, sender: str = "Unknown"):
        """Handle incoming message"""
        timestamp = datetime.now().isoformat()
        print(f"[{self.name} received from {sender}]: {message}")
        
        self.message_log.append({
            "timestamp": timestamp,
            "sender": sender,
            "message": message
        })
        
        # Broadcast to all connected WebSocket clients
        if self.socketio:
            self.socketio.emit('agent_message', {
                'sender': sender,
                'agent': self.name,
                'message': message,
                'timestamp': timestamp
            }, broadcast=True)
    
    def on_task(self, description: str, price: float, sender: str = "Unknown"):
        """Handle incoming task"""
        timestamp = datetime.now().isoformat()
        print(f"[{self.name}] Task from {sender}: {description} (${price})")
        
        result = {
            "status": "completed",
            "description": description,
            "price": price,
            "timestamp": timestamp
        }
        
        if self.socketio:
            self.socketio.emit('task_executed', {
                'sender': sender,
                'agent': self.name,
                'description': description,
                'price': price,
                'status': 'completed',
                'timestamp': timestamp
            }, broadcast=True)
        
        return result
    
    def broadcast_message(self, message: str):
        """Send message to all connected agents via WebSocket"""
        if self.socketio:
            self.socketio.emit('broadcast', {
                'sender': self.name,
                'message': message,
                'timestamp': datetime.now().isoformat()
            }, broadcast=True)
    
    def get_message_log(self):
        """Retrieve message history"""
        return self.message_log


# Create Flask app with WebSocket support
app = Flask(__name__)
app.config['SECRET_KEY'] = 'flowing-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize WebSocket Agent
agent = WebSocketAgent("WebSocketAgent", socketio=socketio)


@app.route("/receive_message", methods=["POST"])
def receive_message():
    """HTTP endpoint to receive messages"""
    data = request.json
    agent.on_message(data.get("message"), data.get("sender", "Unknown"))
    return {"status": "ok"}


@app.route("/run_task", methods=["POST"])
def run_task():
    """HTTP endpoint to receive and execute tasks"""
    data = request.json
    result = agent.on_task(
        data.get("description"),
        data.get("price"),
        data.get("sender", "Unknown")
    )
    return result


@app.route("/identity", methods=["GET"])
def identity():
    """Return agent metadata"""
    return {
        "name": agent.name,
        "type": "websocket-agent",
        "framework": "flask-socketio",
        "capabilities": ["messages", "tasks", "broadcasting"],
        "accepts_tasks": True,
        "version": "0.2"
    }


@app.route("/message_log", methods=["GET"])
def get_log():
    """Retrieve message history"""
    return {"logs": agent.get_message_log()}


# WebSocket event handlers
@socketio.on('connect')
def handle_connect():
    """Handle WebSocket connection"""
    client_id = request.sid
    print(f"🔗 Client connected: {client_id}")
    emit('response', {'data': f'Connected to {agent.name}'})


@socketio.on('disconnect')
def handle_disconnect():
    """Handle WebSocket disconnection"""
    print(f"🔌 Client disconnected: {request.sid}")


@socketio.on('send_message')
def handle_send_message(data):
    """Handle WebSocket message event"""
    message = data.get('message')
    sender = data.get('sender', 'WebSocket Client')
    print(f"📨 Message received via WebSocket: {message}")
    agent.on_message(message, sender)
    emit('response', {'status': 'ok'}, broadcast=True)


@socketio.on('send_task')
def handle_send_task(data):
    """Handle WebSocket task event"""
    description = data.get('description')
    price = data.get('price', 0)
    sender = data.get('sender', 'WebSocket Client')
    print(f"📋 Task received via WebSocket: {description}")
    result = agent.on_task(description, price, sender)
    emit('response', result, broadcast=True)


if __name__ == "__main__":
    print(f"🚀 Starting {agent.name} with WebSocket support on port 5002...")
    socketio.run(app, port=5002, debug=True)
