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
p=getpass("Enter admin password: ")

while (p.lower() != "badwolf"):
    print("Wrong password")
    p=getpass("Enter admin password: ")

call("/Applications/VLC.app/Contents/MacOS/VLC Code1_DGT.mp3 Code2_SBG.mp3 Code3_NL.mp3 &", shell=True)

getpass(riddle1)
p=getpass("Enter shield activation/radiation medecine token: ")

while(p.lower() != "zb93" and p.lower() != "fg79"):
    print("wrong token")
    p=getpass("Enter shield activation/radiation medecine token: ")


getpass(riddle_passed)
cls()


# Riddle #2

print(riddle2)

print("Load a breathable atmosphere into the escape pods. Beware of oxygen toxicity!")
    
O2_level = 0
N2_level = 0
Ar_level = 0
CO2_level = 0
i = 0

while not ((np.abs(O2_level-21) < 2) and (np.abs(N2_level-78) < 2) and (np.abs(Ar_level-1) < 0.5) and (np.abs(CO2_level-0.05) < 0.02)):
    if (i > 0):
        print("Hum, not quite breathable yet...")
        
    mainQuest = menu("Pipe 28, level {:.2f}%".format(N2_level), "Pipe 40, level {:.2f}%".format(Ar_level), "Pipe 20, level 0.00%", "Pipe 26, level 0.00%", "Pipe 04, level 0.00%", "Pipe 84, level 0.00%", "Pipe 44, level {:.2f}%".format(CO2_level), "Pipe 02, level 0.00%", "Pipe 32, level {:.2f}%".format(O2_level))

    if mainQuest == 1:
        try:
            N2_level=float(getpass("Fill pods with gas 28 at (%) "))
        except:
            N2_level = 0

    elif mainQuest == 2:
        try:
            Ar_level=float(getpass("Fill pods with gas 40 at (%) "))
        except:
            Ar_level = 0
            
    elif mainQuest == 7:
        try:
            CO2_level=float(getpass("Fill pods with gas 44 at (%) "))
        except:
            CO2_level = 0
    elif mainQuest == 9:
        try:
            O2_level=float(getpass("Fill pods with gas 32 at (%) "))
        except:
            O2_level=0
            
    else:
        print("No need to breath that, actually!")

    i+=1


getpass(riddle_passed)
cls()

# Riddle #3

print(riddle3)
mainQuest = menu("Sit back, relax and watch interdimensional cable", "Compute escape pods coordinates")

if mainQuest==1:
    print("Connecting to interdimensional cable")    

    for i in tqdm(range(0,100)):
        sleep(0.1)

    print("C137 - XZF8901: link established")
    
    call("open  https://topotech.github.io/interdimensionalcable/", shell=True)

    mainQuest = menu("Compute escape coordinates")

    if mainQuest==1:
        print("Computing escape trajectory")

        for i in tqdm(range(0,100)):
            sleep(0.1)

        call("open escape_map.pdf", shell=True)
        
elif mainQuest==2:
    print("Computing escape trajectory")

    for i in tqdm(range(0,100)):
        sleep(0.1)

    call("open escape_map.pdf", shell=True)

    mainQuest = menu("Sit back, relax and watch interdimensional cable")

    if mainQuest == 1:

        print("Connecting to interdimensional cable")    

        for i in tqdm(range(0,100)):
            sleep(0.1)

        print("C137 - XZF8901: link established")
    
        call("open  https://topotech.github.io/interdimensionalcable/", shell=True)

        
p=getpass("Enter pods escape coordinates [DIMENSION-RADIUS-ANGLE DDDD-RR-AAA]: ")

while(p.lower() != "c137-30-135"):
    print("loading coordinates {}".format(p.lower()))
    for i in tqdm(range(0,10)):
            sleep(0.1)
    
    if (p.lower() == "c137-30-045"):
        print("Not enough fuel for this escape coords")
        p=getpass("Enter pods escape coordinates: DIMENSIONS-RADIUS-ANGLE DDDD-RR-AAA: ")
    else:
        print("Invalid coordinates")
        p=getpass("Enter pods escape coordinates: DIMENSIONS-RADIUS-ANGLE DDDD-RR-AAA: ")


print("Uploading trajectory")
for i in tqdm(range(0,100)):
    sleep(0.1)


getpass(riddle_passed)

getpass(riddle4)

#cls()
#getpass(end)

