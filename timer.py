"""
To do list:
-handle case where user enters blank input for seconds.
    This case should act as zero seconds, instead of an error.
-Add colors to timer (green, yellow for <1:00, red for <0:10
-Currenly each iteration runs for (1 second+code execution time)
    Use timestamps to measure how fr off the timer is
    Look at ways to make it more accurate.
"""

from time import sleep
from pyfiglet import figlet_format as ff
from os import name as osname
from os import system
from colorama import Fore, Back, Style

#enable system to clear screen.
system('')

def screen_clear():
    if osname == "posix":
        _ = system('clear')    
    else:
        _ = system('cls')
       
seconds_valid = False

minutes = int(input('Enter number of minutes:  '))

while not seconds_valid:
    seconds = int(input('Enter number of seconds  '))
    if seconds < 60: seconds_valid=True
    else: print ("Please enter a value less than 60.")

print (Fore.GREEN, Style.BRIGHT)

while minutes >=0:
    while seconds > 0:
        screen_clear()
        text= (f'{minutes}:{seconds:0>2}')
        formtext = ff(text,font='doh')
        
        if minutes == 0 and seconds <=30 and seconds>10: print(Fore.YELLOW)
        if minutes == 0 and seconds <= 10: print(Fore.RED) 
        print (formtext)
        sleep (1)
        seconds -=1
    minutes -= 1
    seconds = 59
    
screen_clear()

formtext = ff("Time up!")

print (formtext)

print (Style.RESET_ALL)
