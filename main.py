#main.py

#imports
import random as rand

#variables + lists
room = "start"
choices = ["placeholder value"]
choice = 1

#functions
def Addchoices():
    global room
    global choices
    if room == "start":
        choices = ["1. Leave the room", "2. Check Computer"]
    if room == "hallway":
        choices = ["1. Containment", "2. Observation", "3. Armory", "4. Exit"]
    if room == "armory":
        choices = ["1. Pistol", "2. Shotgun", "3. Rifle"]
    if room == "facility exterior":
        choices = ["1. Investigate the pond", "2. Go to the town"]
    if room == "town square":
        choices = ["1. Talk to the people", "2. Enter the shop"]

def Pickpath():
    global room
    global choices
    print(*choices, sep="\n")
    print()
    
    if room == "start":
        choice = int(input("What do you do?"))
        if choice == 1:
            room = "hallway"
            print("As you leave the room, the door locks behind you. You look around the hallway and see 4 labled doors.")
        if choice == 2:
            print("You look at the computer screen. It's dammaged beyond repair, but you can make out a <containment breached> error.")

    elif room == "hallway":
        choice = int(input("Which door to go through?"))
        if choice == 1:
            print("When you open the door, you see a pair of glowing red eyes. You quickly slam the door and go back to the hallway.")
        if choice == 2:
            print("You enter the room and see a large glass window with a strange creature inside. It looks like a cross between a lizard and a wolf.")
            print("You quickly go back to the hallway.")
        if choice == 3:
            print("You enter the armory and see a large array of weapons.")
            room = "armory"
        if choice == 4:
            choices = ["1. Investigate the pond", "2. Go to the town"]
            room = "facility exterior"
            print("When you leave the building, you see the ruins of a city in the distance.")
            print("To you left, you see a small pond that looks polluted. To your right, you see a small town that looks abandoned.")

    elif room == "armory":
        choice = int(input("Which weapon do you choose?"))
        if choice == 1:
            weapon = "pistol"
            print("You pick up the pistol and go back to the hallway.")
        if choice == 2:
            weapon = "shotgun"
            print("You pick up the shotgun and go back to the hallway.")
        if choice == 3:
            weapon = "rifle"
            print("You pick up the rifle and go back to the hallway.")
        room = "hallway"

    elif room == "facility exterior":
        choice = int(input("Which way do you go?"))
        print()
        if choice == 1:
            print("You walk up to the pond and look at your reflection. To your surprise, in your reflection, your face looks like it has been replaced with a screen.")
            print("As you look closer, you notice that your head is shaped vaguely like the head of a wolf. You chalk it up to halucinations and go to the town")
            room = "town square"
        elif choice == 2:
            print("You walk into the town and see a group of people. They look at you strangely, but go back to their business.")

    elif room == "town square":
        choice = int(input("What do you do?"))

    print("Press enter to continue")
    a = input()
    print()

#main
print("You see a door and a computer.")
print("You wake up in a dim room.")
while True:
    Addchoices()
    Pickpath()