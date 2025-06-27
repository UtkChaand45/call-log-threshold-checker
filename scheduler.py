import schedule
import time
import subprocess

def run_main():
    try:
        # Run the main.py script
        print("Running main.py job...")
        subprocess.run(["python3", "app/main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running main.py: {e}")

# Schedule every 5 minutes
schedule.every(5).minutes.do(run_main)

if __name__ == "__main__":
    print("Scheduler started. Running main.py every 5 minutes...")
    while True:
        schedule.run_pending()
        time.sleep(1)

# This script uses the `schedule` library to run the `main.py` script every 5 minutes.