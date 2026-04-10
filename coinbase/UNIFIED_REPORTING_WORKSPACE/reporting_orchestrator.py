#!/usr/bin/env python3
"""
reporting_orchestrator.py

A centralized orchestration engine for the UNIFIED_REPORTING_WORKSPACE.
Consolidates multiple independent background loops into a single efficient
sequential pipeline to minimize CPU/IO contention on fanless hosts.

Management:
- Accuracy Reports (30m)
- Transaction Analysis (30m)
- Architecture Documentation (60m)
- Strategy Performance (24h)
- Analytics Master Hub (Post-update)
"""

import os
import sys
import time
import subprocess
import logging
from datetime import datetime, timedelta
from pathlib import Path

# Setup paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

# Task Definitions
TASKS = {
    "accuracy": {
        "scripts": [
            SCRIPT_DIR / "generate_hourly_accuracy_report.py" # Uses --once internally when called with flag
        ],
        "interval_minutes": 30,
        "args": ["--once"]
    },
    "transactions": {
        "scripts": [
            SCRIPT_DIR / "TRANSACTION_ANALYSIS" / "analyze_approved_signals.py",
            SCRIPT_DIR / "TRANSACTION_ANALYSIS" / "generate_transaction_dashboard.py",
            SCRIPT_DIR / "TRANSACTION_ANALYSIS" / "push_transaction_dashboard_to_gh.py"
        ],
        "interval_minutes": 30
    },
    "strategy": {
        "scripts": [
            SCRIPT_DIR / "aggregate_strategy_performance.py",
            SCRIPT_DIR / "generate_strategy_performance_dashboard.py",
            SCRIPT_DIR / "push_strategy_dashboard_to_gh.py"
        ],
        "interval_minutes": 1440
    },
    "docs": {
        "scripts": [
            SCRIPT_DIR / "push_architecture_to_gh.py"
        ],
        "interval_minutes": 60
    },
    "trades": {
        "scripts": [
            SCRIPT_DIR / "generate_trade_summary_dashboard.py"
        ],
        "interval_minutes": 30
    },
    "system": {
        "scripts": [
            PROJECT_ROOT / "scripts" / "remote_status_fetcher.py",
            SCRIPT_DIR / "generate_system_status_dashboard.py"
        ],
        "interval_minutes": 10
    },
    "hub": {
        "scripts": [
            SCRIPT_DIR / "generate_analytics_dashboard.py"
        ],
        "interval_minutes": 0 # Runs after every successful cycle
    }
}

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(PROJECT_ROOT / "logs" / "reporting_orchestrator.log")
    ]
)
logger = logging.getLogger("ReportingOrchestrator")

def run_script(script_path, args=None):
    """Runs a python script as a subprocess."""
    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)
    
    logger.info(f"▶️ Executing: {script_path.name} {' '.join(args or [])}")
    try:
        # We capture output but only show if error or verbose
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if result.stdout:
            # Only print first few lines of stdout to keep logs clean
            lines = result.stdout.strip().split('\n')
            for line in lines[:5]:
                logger.info(f"  [stdout] {line}")
            if len(lines) > 5:
                logger.info(f"  [stdout] ... ({len(lines)-5} more lines)")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Error in {script_path.name}:")
        logger.error(e.stdout)
        logger.error(e.stderr)
        return False

def main():
    logger.info("🚀 Reporting Orchestrator initialized. Monitoring tasks...")
    
    # Track last run times
    last_run = {name: datetime.min for name in TASKS.keys()}
    
    # Breathing gap between tasks (seconds)
    BREATH_GAP = 5

    while True:
        now = datetime.now()
        cycle_performed = False
        
        # 1. Check which task groups need to run
        for task_name, task_cfg in TASKS.items():
            # Skip hub, it runs specially
            if task_name == "hub":
                continue
                
            interval = timedelta(minutes=task_cfg["interval_minutes"])
            if now - last_run[task_name] >= interval:
                logger.info(f"--- Starting Task Group: {task_name.upper()} ---")
                
                success_all = True
                for script in task_cfg["scripts"]:
                    if not run_script(script, task_cfg.get("args")):
                        success_all = False
                        # Break group if a script fails
                        break
                    time.sleep(BREATH_GAP)
                
                if success_all:
                    last_run[task_name] = now
                    cycle_performed = True
                
                logger.info(f"--- Completed Task Group: {task_name.upper()} ---")

        # 2. If any data was updated, refresh the master hub
        if cycle_performed:
            logger.info("✨ Data changes detected. Refreshing Analytics Hub...")
            for script in TASKS["hub"]["scripts"]:
                run_script(script)
                time.sleep(BREATH_GAP)

        # 3. Sleep until next check
        # Check every minute
        time.sleep(60)

if __name__ == "__main__":
    # Ensure logs dir exists
    (PROJECT_ROOT / "logs").mkdir(parents=True, exist_ok=True)
    try:
        main()
    except KeyboardInterrupt:
        logger.info("🛑 Orchestrator stopped by user.")
        sys.exit(0)
