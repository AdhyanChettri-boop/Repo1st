import random


def character():
    global name
    name = input("Enter your name")


while True:
    a = input("Will you enter? (y/n) ").lower()

    if a == 'y':
        print("Welcome to the game")
        character()
        break
    elif a == 'n':
        print("COWARD")
        break
    else:
        print("Don't try to summon the devil and say what you want")


def spawn():
    while True:
        a = int(input("What place do you wanna enter? (1/2) \n1) Forest\n2) House"))
        if a == 1:
            print("Entering the Forest")
            break
        elif a == 2:
            print("Entering the House")
            break
        else:
            print("Error")


def Whispering_Widow():
    dialogues = ["Every step you take… I remember",
                 f"Leaving already{name}? That never works",
                 "You’ve been here before. Not in this game",
                 f"Say it out loud{name}. I’m listening",
                 "I wore your face once"]
    print(random.choice(dialogues))


def Crooked_Child():
    dialogues = ["Slow down… or don’t",
                 "If you don’t look at me, I’ll move",
                 "I’m closer now",
                 f"Don’t blink{name}",
                 "You already lost once",
                 "You remembered me wrong", ]
    print(random.choice(dialogues))
