from datetime import datetime
from datetime import timedelta
import time
import keyboard

current_time=datetime.now()

def show_time():
  
 global current_time
 

 while True:
  
  current_time_formatted=current_time.strftime("%H:%M:%S")

  print("\033[H\033[J", end="")
  print(current_time_formatted)
  print("press X to quit")

  time.sleep(1)
  current_time+=timedelta(seconds=1)

  if keyboard.is_pressed("x"):
   menu()

def define_time(hours, minutes, seconds):
 
 global current_time
 current_time=current_time.replace(hour=hours, minute=minutes, second=seconds)
 
 while True:
 
  print("\033[H\033[J", end="")
  print(current_time.strftime("%H:%M:%S"))
  print("press X to quit")

  time.sleep(1)
  current_time+=timedelta(seconds=1)
 
  if keyboard.is_pressed("x"):
   menu()

def set_alarm(h, m, s):
  global current_time
  global set_time_alarm
 
  while True:
  
    print("\033[H\033[J", end="")
    
    current_time+=timedelta(seconds=1)
    set_time_alarm=current_time.replace(hour=h, minute=m, second=s)
    formatted_time_alarm=set_time_alarm.time().strftime("%H:%M:%S")
   
    print(f"alarm set at: {formatted_time_alarm}")
    print(current_time.strftime("%H:%M:%S"))
    print("press X to quit")
   
    time.sleep(1)
    
    if current_time==set_time_alarm:
      print("your alarm is ringing!") 
      time.sleep(5)
      menu()

    elif keyboard.is_pressed("x"):
      menu()

    else:
      continue
    
def menu():
 global current_time
 global set_time_alarm
 print("Clock menu")
 print("1. Check time")
 print("2. Change time")
 print("3. Set an alarm")
 
 choice=int(input("What do you want to do? 1/2/3: "))
 if choice==1:
    show_time()
 elif choice==2:
    H=int(input("choose an hour: "))
    M=int(input("choose minutes: "))
    S=int(input("choose seconds: "))
    define_time(H,M,S)
 elif choice==3:
    hour_alarm=int(input("choose an hour: "))
    minutes_alarm=int(input("choose minutes: "))
    seconds_alarm=int(input("choose seconds: "))
    set_alarm(hour_alarm, minutes_alarm, seconds_alarm)
   
menu()


  
  


