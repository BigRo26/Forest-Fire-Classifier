#!/usr/bin/env python3
"""
Startup script for Forest Fire Classifier
Runs both Flask backend and React frontend
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def run_command(command, cwd=None, shell=True):
    """Run a command and return the process"""
    try:
        process = subprocess.Popen(
            command,
            cwd=cwd,
            shell=shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return process
    except Exception as e:
        print(f"Error running command '{command}': {e}")
        return None

def main():
    print("🌲 Starting Forest Fire Classifier...")
    print()
    
    # Get project root directory
    project_root = Path(__file__).parent
    
    # Start Flask backend
    print("🚀 Starting Flask Backend...")
    backend_dir = project_root / "backend"
    backend_process = run_command("python app.py", cwd=backend_dir)
    
    if backend_process:
        print("✅ Backend started successfully")
    else:
        print("❌ Failed to start backend")
        return
    
    # Wait a moment for backend to initialize
    print("⏳ Waiting for backend to initialize...")
    time.sleep(3)
    
    # Start React frontend
    print("⚛️  Starting React Frontend...")
    frontend_dir = project_root / "frontend"
    frontend_process = run_command("npm start", cwd=frontend_dir)
    
    if frontend_process:
        print("✅ Frontend started successfully")
    else:
        print("❌ Failed to start frontend")
        backend_process.terminate()
        return
    
    print()
    print("🎉 Both services are running!")
    print("📍 Backend: http://localhost:5000")
    print("📍 Frontend: http://localhost:3000")
    print()
    print("Press Ctrl+C to stop all services...")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping services...")
        
        if backend_process:
            backend_process.terminate()
            print("✅ Backend stopped")
        
        if frontend_process:
            frontend_process.terminate()
            print("✅ Frontend stopped")
        
        print("👋 Goodbye!")

if __name__ == "__main__":
    main()


