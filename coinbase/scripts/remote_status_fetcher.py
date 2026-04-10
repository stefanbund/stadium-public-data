#!/usr/bin/env python3
import subprocess
import json
import os
import sys
from datetime import datetime

# --- Configuration ---
REMOTE_USER = "stefanbund"
REMOTE_HOST = "stefans-Mac-mini.local"
REMOTE_LOG_PATH = "/Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/logs/watchdog_MLOps_Orchestrator.log"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "logs", "remote_status.json")

def fetch_remote_status():
    """Fetches system metrics and log tail from the remote Mac Mini."""
    
    # Commands to run on remote
    remote_cmds = (
        "echo '{\"cpu\": '$(ps -A -o %cpu | awk '{s+=$1} END {print s}')', "
        "\"mem\": '$(ps -A -o %mem | awk '{s+=$1} END {print s}')', "
        "\"uptime\": \"'$(uptime | awk -F', ' '{print $1}')'\", "
        "\"log_tail\": \"'$(tail -n 10 " + REMOTE_LOG_PATH + " | base64)'\"}'"
    )
    
    ssh_cmd = [
        "ssh",
        f"{REMOTE_USER}@{REMOTE_HOST}",
        remote_cmds
    ]
    
    try:
        result = subprocess.run(ssh_cmd, capture_output=True, text=True, timeout=15)
        if result.returncode == 0:
            status_data = json.loads(result.stdout)
            # Add timestamp and host
            status_data["timestamp"] = datetime.now().isoformat()
            status_data["host"] = REMOTE_HOST
            status_data["status"] = "ONLINE"
            
            # Write to local file
            os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
            with open(OUTPUT_FILE, "w") as f:
                json.dump(status_data, f, indent=4)
            print(f"✅ Remote status for {REMOTE_HOST} updated.")
        else:
            raise Exception(result.stderr)
    except Exception as e:
        # Write offline status
        status_data = {
            "timestamp": datetime.now().isoformat(),
            "host": REMOTE_HOST,
            "status": "OFFLINE",
            "error": str(e)
        }
        with open(OUTPUT_FILE, "w") as f:
            json.dump(status_data, f, indent=4)
        print(f"❌ Could not reach {REMOTE_HOST}: {e}")

if __name__ == "__main__":
    fetch_remote_status()
