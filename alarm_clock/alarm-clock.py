import time

def set_alarm():
    hour = int(input("please enter the hour (0-23): "))
    minute = int(input("please enter the minute (0-59): "))
    second = int(input("please enter the second (0-59): "))
    print(f"alarm set for {hour}:{minute}:{second}")
    total_seconds = hour*3600 + minute*60 + second
    print("waiting...")
    for i in range(total_seconds + 1):
        time.sleep(1)
        if time.strftime("%H:%M:%S") == f"{hour}:{minute}:{second}":
            print("Time to wake up!")
            break

set_alarm()
