import time

def alarm():
    hours = input("enter the amount of hours, ")
    minutes = input("enter the amount of minutes, ")
    seconds = input("enter the amount of seconds, ")

    if hours == "0" or hours == "":
        if (minutes) == "0" or minutes == "":
            if (seconds) == "0" or seconds == "":
                print("Please enter a valid time")
                alarm()
            elif (seconds) != "0":
                print("Alarm is set for", seconds, "seconds")
                time.sleep((int(seconds)))
                print("Time's up")
            else:
                print("please enter a valid input")
                alarm()
        elif (minutes) != "0":
            minutes_to_seconds = int(minutes) * 60
            if (seconds) == "0" or seconds == "":
                print(f"Alarm is set for {minutes} minutes")
                time.sleep(minutes_to_seconds)
                print("Time's up")
            elif (seconds) != "0":
                total_seconds = minutes_to_seconds + int(seconds)
                print(f"Alarm is set for {minutes} minutes and {seconds} seconds")
                time.sleep(total_seconds)
                print("Time's up")
            else:
                print("please enter a valid input")
                alarm()
        else:
            print("please enter a valid input")
            alarm()
    elif (hours) != "0":
        hours_to_minutes = int(hours) * 3600
        if (minutes) == "0" or minutes =="":
            if (seconds) == "0" or seconds == "": 
                print(f"Alarm is set for {hours} hours")
                time.sleep(hours_to_minutes)
            elif (seconds) != "0":
                print(f"Alarm is set for {hours} hour and {seconds} second")
                time.sleep(hours_to_minutes + int(seconds))
                print("Time's up")
            else:
                print("please enter a valid input")
                alarm()
        elif (minutes) != "0":
            minutes_to_seconds = int(minutes) * 60
            if (seconds) == "0" or seconds == "":
                print(f"Alarm is set for {hours} hours and {minutes} minutes")
                time.sleep(hours_to_minutes + minutes_to_seconds)
                print("Time's up")
            elif (seconds) != "0":
                print(f"Alarm is set for {hours} hour {minutes} minutes and {seconds} seconds")
                time.sleep(hours_to_minutes + minutes_to_seconds + int(seconds))
                print("Time's up")
            else:
                print("please enter a valid input")
                alarm()
        else:
            print("please enter a valid input")
            alarm()
    else:
        print("please enter a valid input")
        alarm()

alarm()