import datetime
from selenium import webdriver
import schedule
import time
from join import *
from info import *

today = datetime.datetime.now()
weekday= (today.strftime("%a"))

def monday():
    schedule.every().tuesday.at(lecOneT).do(subj1)        
    print("Scheduled successfully")

def tuesday():
    schedule.every().tuesday.at(lecOneT).do(subj2)      
    print("Scheduled successfully")

def wednesday():
    schedule.every().wednesday.at(lecOneT).do(subj3)
    print("Scheduled successfully")

def thursday():
    schedule.every().thursday.at(lecOneT).do(subj1)
    print("Scheduled successfully")

def friday():
    schedule.every().friday.at(lecOneT).do(subj2)      
    print("Scheduled successfully")

def saturday():
    schedule.every().saturday.at(lecOneT).do(subj3)        
    print("Scheduled successfully")
    

# Code for Timetable.py ends here 

if weekday=="Mon":
    monday()
    print("checked succesfully")
elif weekday=="Tue":
    tuesday()
    print("checked succesfully")
elif weekday=="Wed":
    wednesday()
    print("checked succesfully")
elif weekday=="Thu":
    thursday()
    print("checked succesfully")
elif weekday=="Fri":
    friday()
    print("checked succesfully")
elif weekday=="Sat":
    saturday()
    print("checked succesfully")
else:
    print("Its sunday bro")
    
while True:
    schedule.run_pending()
    time.sleep(1)
    #seconds