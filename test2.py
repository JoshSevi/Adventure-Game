import time
import sys


class Player:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.age = ''
        self.origin = ''


player1 = Player()


def typewriter(i):
    for char in i:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

    question2 = "Young, Adult, or Elderly?\n"
    typewriter(question2)
    age = input("> ")
    player1.age = age.lower()

    # Identifies what type of memories the player is having and gives a related-sounding string.
    if player1.age == 'young':
        age_string = "Good. That'll make it easier for me."
    elif player1.age == 'adult':
        age_string = "No? Hehehe. You really are troublesome right up to the very end, aren't you?\n"
        typewriter(age_string)
    else:
        age_string = "As I suspected... You don't seem to be the true owner of this story. Goodbye."
        typewriter("Well then, " + player1.name + ", " + age_string + ".")
        quit()


    # Combines all the above parts.
    question3 = "Well then, " + player1.name + ", " + age_string + ".\n"
    typewriter(question3)
    time.sleep(2)
