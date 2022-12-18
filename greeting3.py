#!/usr/bin/python3
import random

from datetime import datetime, time


name=input("Enter your name: ")
greeting_type=input("{}, What kind of greeting would you like? time-based, normal, or random ".format(name))
if greeting_type == 'time-based':
  time_confirmation=input("{}, would you like the current time? yes or no ".format(name))
  now = datetime.now()
  now_time = now.time()
  if time_confirmation == "yes":
    print(now.strftime("{}, the time right now is %H:%M".format(name)))  
  if now_time >= time(6,00) and now_time < time(12,00):
    # morning
    greeting = "Good morning, {} 🐓🌅🥣!".format(name)
  elif now_time == time(12,00):
    # noon
    greeting = "How's your noon, {} 🥪?".format(name)
  elif now_time > time(12,00) and now_time < time(17,00):
    # afternoon
    greeting = "Good afternoon, {}!".format(name)
  elif now_time >= time(17,00) and now_time < time (20,00):
    # evening
    greeting = "Good evening, {}!".format(name)
  else:
    # night
    greeting = "Goodnight, {} 🌙😴💤!".format(name)

  print(greeting)
elif greeting_type == 'normal':
  print("hi, {}".format(name))
elif greeting_type == 'random':
  greetings_list=["Hello","Hi","Good Day","How are you doing","Hola","yo"]
  greeting=random.choice(greetings_list)

  print("{}, {}".format(greeting,name))
else:
  print("Sorry, I don't know that kind of greeting")


