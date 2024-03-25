import datetime
import time

def get_alarm_time():
    """ Ask the user for the time they want to set the alarm for."""
    while True:
        alarm_time = input("Set the alarm time (format HH : MM)> ")
        try:
            #try to parse the input time
            valid_time = datetime.datetime.strptime(alarm_time, "%H:%M")
            return valid_time.time()
        except ValueError:
            print("Invalid format, please use HH : MM.")
            
def main():
    alarm_time = get_alarm_time()
    print(f"Alarm set for {alarm_time.hour}:{alarm_time.minute}.")
    
    while True:
        now = datetime.datetime.now().time()
        #compare current time with alarm time