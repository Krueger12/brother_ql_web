#!/bin/bash

# Function to terminate background processes
cleanup() {
    echo "Terminating background processes..."
    pkill -f brother_ql_web
    pkill -f cli_tool
    exit 0
}

# Trap SIGINT (Ctrl+C) and call cleanup function
trap cleanup SIGINT

# Create a virtual environment
python3 -m venv /home/hbk/private/shift-print/brother_ql_web/venv

# Navigate to the project directory
cd /home/hbk/private/shift-print/brother_ql_web

# Activate the Python virtual environment
source venv/bin/activate

# Print a message indicating the virtual environment is activated
echo "Virtual environment activated."

# Make sure the pip packages are installed
pip install -r /home/hbk/private/shift-print/brother_ql_web/requirements.txt
pip install .

# Start the brother_ql_web service
python -m brother_ql_web --configuration /home/hbk/private/shift-print/brother_ql_web/config.json &

# Start the cli_tool service
python /home/hbk/private/shift-print/brother_ql_web/cli_tool/main.py 

# Wait for background processes to finish
wait