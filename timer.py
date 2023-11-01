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

#enables console to interpret ANSI escape codes.
system('')

def screen_clear():
        if osname == "posix":
            _ = system('clear')    
        else:
            _ = system('cls')

def textcolor(color):
    colorval = 0
    match color:
        case "red":
            colorval = 31
        case "green":
            colorval = 32
        case "yellow":
            colorval = 33
        case "blue":
            colorval = 34
        case "purple":
            colorval = 35
        case "cyan":
            colorval = 36
        case "white":
            colorval = 37
        case _:
            raise ValueError('invalid color')
    print (f"\033[1;{colorval}0;40m\n")
        
minutes = int(input('Enter number of minutes:  '))

seconds_valid = False

#enables console to interpret ANSI escape codes.


while not seconds_valid:
    seconds = int(input('Enter number of seconds  '))
    if seconds < 60: seconds_valid=True
    else: print ("Please enter a value less than 60.")

#print (f'Timer will be set for {minutes} : {seconds}')

textcolor ("cyan")

while minutes >=0:
    while seconds > 0:
        screen_clear()
        text= (f'{minutes}:{seconds:0>2}')
        formtext = ff(text,font='doh')
        print (formtext)
        sleep (1)
        seconds -=1
    minutes -= 1
    seconds = 59
    
screen_clear()

formtext = ff("Time up!")

print (formtext)
