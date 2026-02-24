#!/bin/bash

echo "🚀 Installing Flowing..."

# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "✅ Installation complete."
echo "Starting demo..."

# Run demo automatically
./run.sh
