# project: Task Manager with Date and Time Reminder

# module: Task Manager with Date and Time Reminder
from datetime import datetime
import time

task = input("Enter a task: ")

task_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
task_time = datetime.strptime(task_time_str, "%Y-%m-%d %H:%M")

current_time = datetime.now()
time_left = task_time - current_time

if time_left.total_seconds() <= 0:
    print("❌ Time already passed!")
else:
    seconds_left = int(time_left.total_seconds())

    print(f"⏳ Time left for '{task}': {seconds_left // 60} minutes")

    time.sleep(seconds_left)

    print(f"\n🔔 Reminder: It's time to {task}!")