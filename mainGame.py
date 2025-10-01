# Importing art
from asciiArt import *

# Importing modules
import os
import numpy as np
from getpass import getpass
from subprocess import call
from time import sleep
from tqdm import tqdm

class Format:
    end = '\x1B[0m'
    underline = '\x1B[4m'


# \\\\\\\\ ** FUNCTIONS!!! ** \\\\\\\

# Menu options:
#def menu(choice1 = "", choice2 = "", choice3 = "", choice4 = "", choice5 = ""):
#    myList = [choice1, choice2, choice3, choice4, choice5]

def menu(*options):

    myList = [opt for opt in options]
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
                print(not_an_option)
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

getpass(intro_text1)
getpass(intro_text2)
getpass(intro_text3)
getpass(intro_text4)
getpass(intro_text5)

# Riddle #1
p=getpass(riddle1_passwd)

while (p.lower() != "badwolf"):
    print(riddle1_wrongpasswd)
    p=getpass(riddle1_passwd)

call("/Applications/VLC.app/Contents/MacOS/VLC Code1_DGT.mp3 Code2_SBG.mp3 Code3_NL.mp3 &", shell=True)

getpass(riddle1)
p=getpass(riddle1_shieldtoken)

while(p.lower() != "zb93" and p.lower() != "fg79"):
    print(riddle1_wrongtoken)
    p=getpass(riddle1_shieldtoken)

getpass(riddle_passed)
cls()

# Riddle #2

print(riddle2)

print(riddle2_atmo)
    
O2_level = 0
N2_level = 0
Ar_level = 0
CO2_level = 0
i = 0

while not ((np.abs(O2_level-21) < 2) and (np.abs(N2_level-78) < 2) and (np.abs(Ar_level-1) < 0.5) and (np.abs(CO2_level-0.05) < 0.02)):
    if (i > 0):
        print(riddle2_tmp)
        
    mainQuest = menu(riddle2_pipe.format(28, N2_level),
                     riddle2_pipe.format(40, Ar_level),
                     riddle2_pipe.format(20, 0),
                     riddle2_pipe.format(26, 0),
                     riddle2_pipe.format( 4, 0),
                     riddle2_pipe.format(84, 0),
                     riddle2_pipe.format(44, CO2_level),
                     riddle2_pipe.format( 2, 0),
                     riddle2_pipe.format(32, O2_level))

    if mainQuest == 1:
        try:
            N2_level=float(getpass(riddle2_fill.format(28)))
        except:
            N2_level = 0

    elif mainQuest == 2:
        try:
            Ar_level=float(getpass(riddle2_fill.format(40)))
        except:
            Ar_level = 0
            
    elif mainQuest == 7:
        try:
            CO2_level=float(getpass(riddle2_fill.format(44)))
        except:
            CO2_level = 0
    elif mainQuest == 9:
        try:
            O2_level=float(getpass(riddle2_fill.format(32)))
        except:
            O2_level=0
            
    else:
        print(riddle2_noneed)

    i+=1


getpass(riddle_passed)
cls()

# Riddle #3

print(riddle3)
mainQuest = menu(riddle3_sit_back, riddle3_compute)

if mainQuest==1:
    print(riddle3_connect)

    for i in tqdm(range(0,100)):
        sleep(0.1)

    print(riddle3_link)
    
    call("open  https://topotech.github.io/interdimensionalcable/", shell=True)

    mainQuest = menu(riddle3_compute)

    if mainQuest==1:
        print(riddle3_escape)

        for i in tqdm(range(0,100)):
            sleep(0.1)

        call("open escape_map.pdf", shell=True)
        
elif mainQuest==2:
    print(riddle3_escape)

    for i in tqdm(range(0,100)):
        sleep(0.1)

    call("open escape_map.pdf", shell=True)

    mainQuest = menu(riddle3_sit_back)

    if mainQuest == 1:

        print(riddle3_connect)

        for i in tqdm(range(0,100)):
            sleep(0.1)

        print(riddle3_link)
    
        call("open  https://topotech.github.io/interdimensionalcable/", shell=True)

p=getpass(riddle3_coords)

while(p.lower() != "c137-30-135"):
    print(riddle3_loading.format(p.lower()))
    for i in tqdm(range(0,10)):
            sleep(0.1)

    if (p.lower() == "c137-30-045"):
        print(riddle3_fuel)
        p=getpass(riddle3_coords)
    else:
        print(riddle3_invalid)
        p=getpass(riddle3_coords)


print(riddle3_uploading)
for i in tqdm(range(0,100)):
    sleep(0.1)


getpass(riddle_passed)

getpass(riddle4)

#cls()
#getpass(end)

