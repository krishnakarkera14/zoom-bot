import time
from selenium import webdriver
import keyboard
from info import *

#download chrome driver and paste full path
driver = webdriver.Chrome(r'C:\Users\')

def subj1():
    driver.get(exampleLec1)
    time.sleep(7)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(3000)
    driver.quit()

def subj2():
    driver.get(exampleLec2)
    time.sleep(7)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(3000)
    driver.quit()

def subj3():
    driver.get(exampleLec3)
    time.sleep(7)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(3000)
    driver.quit()


