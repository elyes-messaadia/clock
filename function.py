from datetime import datetime
from datetime import timedelta
from display import *

def running_hour(current_time, is_paused):
  if not is_paused:
    return current_time+timedelta(seconds=1)
  return current_time
 
def define_time(current_time, hours, minutes, seconds):
 return current_time.replace(hour=hours, minute=minutes, second=seconds)

def set_alarm(h, m, s): 
 return h, m, s

def reset_time():
  return datetime.now()   

def change_time(time_format):
  
  if time_format=="24h":
     return "12h"
  elif time_format=="12h":
     return "24h"

def paused(is_paused):
  return not is_paused

def check_time_alarm(current_time, set_time_alarm):
    
    if set_time_alarm is None:
       return False
    
    h, m, s=set_time_alarm

    if (current_time.hour, current_time.minute, current_time.second)==(h, m, s):
        print("your alarm is ringing!")
        return True
    return False
    
def check_hour():
 while True:
  try:
       H=int(input("choose an hour: "))
       if H in range(0,24):
         return H
       print("Invalid number! Choose 0-23 for hours!")
  except ValueError:
        print("Enter numbers only!")
  
def check_minutes():
 while True:
  try: 
       M=int(input("choose minutes: "))
       if M in range(0,60):
          return M
       print("Invalid number! Choose 0-59 for minutes!")  
    
  except ValueError:
        print("Enter numbers only!")
      
def check_seconds():
 while True:
  try:
      S=int(input("choose seconds: "))
      if S in range(0,60):
         return S
      print("Invalid number! Choose 0-59 for seconds!") 
  except ValueError:
        print("Enter numbers only!")
    