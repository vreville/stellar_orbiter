# Importing art
from asciiArt import *

# Importing modules
import os
from getpass import getpass
from subprocess import call
from time import sleep
from tqdm import tqdm

class Format:
    end = '\x1B[0m'
    underline = '\x1B[4m'


# \\\\\\\\ ** FUNCTIONS!!! ** \\\\\\\

# Menu options:
def menu(choice1 = "", choice2 = "", choice3 = "", choice4 = "", choice5 = ""):
    myList = [choice1, choice2, choice3, choice4, choice5]
    letterStart = 64
    index = -1
    correctAnswer = False
    listOfChoices = []
    answer = ""
    print("-----------------")
    
    for item in myList:
        index += 1
        letterStart += 1
        if item == "": 
            continue
        print(chr(letterStart) + ") " + item)
        listOfChoices.append(chr(letterStart))
        sleep(0.3)
    print("-----------------")

    while correctAnswer == False:
        try:
            answer = input("> ")
            answer = answer.upper()
            if listOfChoices.index(answer) != -1:
                correctAnswer = True
                return(listOfChoices.index(answer)+1)
        except ValueError:
            if answer == "":
                continue
            else:
                print("")
                print("Sorry, that's not an option!")
                print("")
    print("")
    

# Clear the screen:
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# Animations:
# This function gets the first frame you want to show up. Then it gets the 
# second frame you want to appear. Next, it gets the time between each frame. 
# And lastly, the 'loops' (how many times you want the animation to repeat).
def animation(frame1, frame2, timeBetweenFrames, loops):
    for i in range(loops):
        print(frame1)
        
        sleep(timeBetweenFrames)
        
        cls()
        
        print(frame2)
        
        sleep(timeBetweenFrames)
        
        cls()


# Animating text:
def textAnimation(sentence, timeBetweenLetters=0.02):
    chars = sentence
    loop = range(1, len(chars) + 1)
    
    for idx in loop:
        print(chars[:idx], end='\r') # <-- end with carriage return
        sleep(timeBetweenLetters)
    print("")
 
# Game Over screen:
def gameOver(time, sentence=""):
    cls()
    print("""

  /$$$$$$                                   
 /$$__  $$                                  
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
 \______/  \_______/|__/ |__/ |__/ \_______/
    """)
    
    sleep(time)
    
    print("""
  /$$$$$$                               
 /$$__  $$                              
| $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/     \_/    \_______/|__/      
                                        
    """)
    
    sleep(0.25)
    
    textAnimation(sentence)
    quit()

            
# Make background go black (only for web Python interpreters):  
def blackground(sentence = ""):
    print('\x1b[40m''\x1b[97m')
    print(" " * 9999)
    cls()


# Make background go white (only for web Python interpreters):     
def whiteBackground(sentence = ""):
    print('\u001b[0m')
    print(" " * 9999)
    cls()


# ------------ GAME INTRODUCTION -------------------------:

getpass(title) 

#getpass(kerrigan)
getpass(intro_text1)
getpass(intro_text2)
getpass(intro_text3)
getpass(intro_text4)
getpass(intro_text5)

#animation(animationLetter1, animationLetter2, 0.3, 5)

p=getpass("Enter admin password: ")

while (p.lower() != "caca"):
    print("Wrong password")
    cls()
    p=getpass("Enter admin password: ")

p=getpass("Enter shield activation token: ")

while(p.lower() != "boudin"):
    print("wrong token")
    p=getpass("Enter shield activation token: ")


mainQuest = menu("Sit back, relax and watch interdimensional cable", "Compute escape coordinates", "Call a friend")
print(mainQuest)

if mainQuest==1:
    print("Connecting to interdimensional cable")    

    for i in tqdm(range(0,100)):
        sleep(0.1)

    print("C 137 - XZF 8901: link established")
    
    call("open  https://topotech.github.io/interdimensionalcable/", shell=True)

    mainQuest = menu("Compute escape coordinates", "Call a friend")


elif mainQuest==2:
    print(mainQuest)
    print("Computing escape trajectory")

    for i in tqdm(range(0,100)):
        sleep(0.1)

    call("open escape_map.pdf", shell=True)

    menu("Sit back, relax and watch interdimensional cable", "Call a friend")

    mainQuest = menu("Compute escape coordinates", "Call a friend")

    
        
p=getpass("Enter pods escape coordinates: DIMENSION-RADIUS-ANGLE DDDD-RR-AAA: ")

while(p.lower() != "c137-25-135"):
    print(p.lower())
    if (p.lower() == "c137-25-045"):
        print("Not enough fuel for this escape coords")
        p=getpass("Enter pods escape coordinates: DIMENSIONS-RADIUS-ANGLE DDDD-RR-AAA: ")
    else:
        print("Invalid coordinates")
        p=getpass("Enter pods escape coordinates: DIMENSIONS-RADIUS-ANGLE DDDD-RR-AAA: ")


print("Uploading trajectory")

getpass(end)

