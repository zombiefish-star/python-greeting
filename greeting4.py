#!/usr/bin/python3
import random


from datetime import datetime, time
now = datetime.now()
now_time = now.time()

if now_time > time(6,00) and now_time < time(12,00):
   morning
  greeting = "Good morning!"
elif now_time == time(12,00):
   noon
  greeting = "How's your noon?"
elif now_time > time(12,00) and now_time < time(18,00):
   afternoon
  greeting = "Good afternoon!"
elif now_time > time(18,00) and now_time < time (20,00):
   evening
  greeting = "How's your evening?"
else:
   night
  greeting = "Good night!"


name=input("Enter your name: ")


#print("hi, {}".format(name))

# greetings_list=["Hello","Hi","Good Day","How are you doing","Hola","yo"]
# greeting=random.choice(greetings_list)

print("{}, {}".format(greeting,name))

