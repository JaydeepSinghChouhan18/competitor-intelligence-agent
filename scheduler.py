import schedule
import time
import subprocess


def run_agent():

    subprocess.run(
        ["python", "main.py"]
    )


schedule.every().day.at(
    "09:00"
).do(run_agent)

while True:

    schedule.run_pending()

    time.sleep(60)