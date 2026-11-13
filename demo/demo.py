#demo.py

#imports
import random as rand

#variables, lists
room = "start" #starting room
choices = ["placeholder value"]
choice = 1 #placeholder value
weapon = "none" #starting weapon
difficulty = 5 #determines hit chance in combat (1 is best chances, 10 is worst chances)
health = 10 #starting health

#functions
def Addchoices():
    global room
    global choices
    if room == "start": #choices for the starting room
        choices = ["1. Leave the room", "2. Check Computer"]
    if room == "hallway": #choices for the hallway
        choices = ["1. Containment", "2. Observation", "3. Armory", "4. Exit"]
    if room == "armory": #choices for the armory
        choices = ["1. Pistol", "2. Shotgun", "3. Rifle"]
    if room == "facility exterior": #choices for the facility exterior
        choices = ["1. Investigate the pond", "2. Go to the town"]
    if room == "town square": #choices for the town square
        choices = ["1. Talk to the people", "2. Enter the shop", "3. Go into the forest"]
    if room == "forest": #choices for the forest
        choices = ["1. Fight the wolves", "2. Run away"]
    if room == "combat": #choices for combat
        choices = ["1. Fight", "2. Negotiate", "3. Run"]

def Combat(): #math and if statements for combat
    global room
    global choices
    global weapon
    global difficulty
    global health

    if weapon != "none":
        print("You have a ", weapon, ".")
    for i in range(health): #loops until the player or the enemy is defeated
        if i > 0:
            print(*choices, sep="\n")
        choice = int(input("What do you do?"))
        if choice == 1:
            if weapon != "none":
                print("You attack the enemy with your ", weapon, ".")
            if rand.randint(1+i, 10) > difficulty: #checks for hit and increases win chance with each turn
                print("You hit the enemy and they take damage.")
                print("Battle Won! You have defeated the enemy.")
                return
            else:
                print("You miss the enemy and they take no damage.")
                print("The enemy attacks you and you take damage.")
                health = health - 1
        elif choice == 2:
            print("You try to act friendly towards the enemy.")
            if rand.randint(1+i, 10) > difficulty: #checks for hit and increases win chance with each turn
                print("The enemy seem to understand you and they stop attacking you.")
                return
            else:
                print("The enemy doesn't understand you and they continue to attack you.")
            print("The enemy attacks you and you take damage.")
            health = health - 1
        elif choice == 3:
            print("You try to run away from the enemy.")
            if rand.randint(1+i, 10) > difficulty: #checks for hit and increases win chance with each turn
                print("You successfully run away from the enemy.")
                return
            else:
                print("You fail to run away from the enemy and they continue to attack you.")
                print("The enemy attacks you and you take damage.")
                health = health - 1
        if health <= 0: #detects when health is 0 or less and ends the game
            print("You have been defeated by the enemy.")
            print("Game Over.")
            exit()

#main
print("You wake up in a dim room.")
print("You see a door and a computer.")
while True:
    Addchoices() #fills the choices list with the appropriate choices for the current room
    print(*choices, sep="\n")
    print()
    
    if room == "start":
        choice = int(input("What do you do?"))
        if choice == 1:
            room = "hallway"
            print("As you leave the room, the door locks behind you. You look around the hallway and see 4 labled doors.")
        elif choice == 2:
            print("You look at the computer screen. It's dammaged beyond repair, but you can make out a <containment breached> error.")

    elif room == "hallway":
        choice = int(input("Which door to go through?"))
        if choice == 1:
            print("When you open the door, you see a pair of glowing red eyes. You quickly slam the door and go back to the hallway.")
        elif choice == 2:
            print("You enter the room and see a large glass window with a strange creature inside. It looks like a cross between a lizard and a wolf.")
            print("You quickly go back to the hallway.")
        elif choice == 3:
            print("You enter the armory and see a large array of weapons.")
            room = "armory"
        elif choice == 4:
            choices = ["1. Investigate the pond", "2. Go to the town"]
            room = "facility exterior"
            print("When you leave the building, you see the ruins of a city in the distance.")
            print("To you left, you see a small pond that looks polluted. To your right, you see a small town that looks abandoned.")

    elif room == "armory":
        choice = int(input("Which weapon do you choose?"))
        if choice == 1:
            weapon = "pistol"
            print("You pick up the pistol and go back to the hallway.")
        elif choice == 2:
            weapon = "shotgun"
            print("You pick up the shotgun and go back to the hallway.")
        elif choice == 3:
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
            room = "town square"
            print("You walk into the town and see a group of people. They look at you strangely, but go back to their business.")

    elif room == "town square":
        choice = int(input("What do you do?"))
        print()
        if choice == 1:
            print("You walk up to the people and ask them what happened to the town. They look at you strangely and say that they don't know what you're talking about.")
            print("You ask them if they know where you are, and they say that you're in a town called 'New Haven'.")
            print("You ask them if they know how to get out of the town, and they say that the only way out is through the forest.")
            print("You thank them for their help.")
        elif choice == 2:
            print("You walk into the shop and see a man behind the counter. He looks at you strangely and says that he doesn't have anything to sell you.")
            print("You ask him if he knows how to get out of the town, and he says that the only way out is through the forest.")
            print("You thank him for his help.")
        elif choice == 3:
            print("You walk into the forest and see a path that leads deeper into the woods. You follow the path and eventually come to a clearing.")
            room = "forest"

    elif room == "forest":
        print("As you enter the clearing, you see a group of what appears to be wolves with scales instead of fur.")
        print("They look at you with glowing red eyes and start to approach you.")
        print("You are now in combat.")
        room = "combat"

    elif room == "combat":
        Combat()
        print("Congratulations, you have completed the demo. Thank you for playing.")
        print("Press enter to exit.")
        if input() == "":
            exit()

    print("Press enter to continue")
    a = input()
    print()
