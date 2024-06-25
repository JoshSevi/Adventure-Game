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
        age_string = "Ah... whether you were fortunate or not... To know this story came from a child... I'm sorry"
    elif player1.age == 'adult':
        age_string = "So your story began at the height of your life? How lucky of you"
    elif player1.age == 'elderly':
        age_string = "Fate chose you, regardless of age. Your strength might have waned but your wisdom was greater than ever"
    else:
        age_string = "That is not an acceptable sign, please try again.\n"
        typewriter(age_string)
        age = input("> ")
        player1.age = age.lower()

# Combines all the above parts.
    question5 = age_string + ".\n"
    typewriter(question5)
    time.sleep(2)