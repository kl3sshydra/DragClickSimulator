# DragClickSimulator
# coded by kl3sshydra
# please dont steal this code


from pynput.mouse import Listener
from datetime import datetime
from threading import Thread
import time
import os

controller = 'Button.button8'
LEFTcontroller = 'Button.button9'


counter = int(input("Cps per thread\n-> "))
multiplier = int(input("Threads\n-> "))
global delay
delay = float(input("Delay between clicks\n-> "))
os.environ['clicked'] = '0'

global logs
logs = input('Do you want to enable logs? [y/n]\n-> ')
logs = logs.lower()
if logs == "y":
    print("Logs will be shown to screen.")
    logstatus = "shown on screen."
else:
    print("Logs will be hidden.")
    logstatus = "not shown on screen."

time.sleep(1.5)
os.system("clear")


print(f"""
╔╦╗┬ ┬┌─┐                
 ║ ├─┤├┤                 
 ╩ ┴ ┴└─┘                
╔╦╗┬─┐┌─┐┌─┐             
 ║║├┬┘├─┤│ ┬             
═╩╝┴└─┴ ┴└─┘             
╔═╗┬  ┬┌─┐┬┌─            
║  │  ││  ├┴┐            
╚═╝┴─┘┴└─┘┴ ┴            
╔═╗┬┌┬┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐
╚═╗│││││ ││  ├─┤ │ │ │├┬┘
╚═╝┴┴ ┴└─┘┴─┘┴ ┴ ┴ └─┘┴└─
[Coded by kl3sshydra]

------- STATS ---------------------
Cps per thread   ->  {counter}
Thread per click ->  {multiplier}
Delay for clicks ->  {delay}
Logs will be     ->  {logstatus}
-----------------------------------

Listening for keys...
""")



def thread1():
    for x in range(counter):
        time.sleep(delay)
        os.system("xdotool click 3")

def start():
    for threadcounter in range(multiplier):
        string1 = f"th{threadcounter} = Thread(target=thread1)"
        string2 = f"th{threadcounter}.start()"
        exec(string1)
        exec(string2)


def thread2():
    for x in range(counter):
        os.system("xdotool click 1")

def LEFTstart():
    for threadcounter in range(multiplier):
        string1 = f"th{threadcounter} = Thread(target=thread2)"
        string2 = f"th{threadcounter}.start()"
        exec(string1)
        exec(string2)


def clicca(x, y, button, pressed):
    getClicked = os.getenv('clicked')    
    if str(button) == controller:
        if getClicked == "0":
            if logs == "y":
                print(f"Clicked with (RIGHT) {controller} at -> [{datetime.now()}]")
            os.environ['clicked'] = '1'
            start()
        else:
            os.environ['clicked'] = '0'
            if logs == "y":
                print(f"Duplicated (RIGHT) clicks at -> [{datetime.now()}]")

    if str(button) == LEFTcontroller:
        if getClicked == "0":
            if logs == "y":
                print(f"Clicked with (LEFT) {controller} at -> [{datetime.now()}]")
            os.environ['clicked'] = '1'
            LEFTstart()
        else:
            os.environ['clicked'] = '0'
            if logs == "y":
                print(f"Duplicated (LEFT) clicks at -> [{datetime.now()}]")


with Listener(on_click=clicca) as listener:
    listener.join()
