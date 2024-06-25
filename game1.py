import sys
import os
import time

screen_width = 100


################
# Player Setup #
################
class Player:
    def __init__(self):
        self.name = ''
        self.memories = ''
        self.age = ''
        self.origin = ''


player1 = Player()


################
# Title Screen #
################
def title_screen_options():
    # Allows the player to select the menu options, case-insensitive.
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "quit":
        sys.exit()
    elif option.lower() == "help":
        help_menu()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Invalid command, please try again.")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "quit":
            sys.exit()
        elif option.lower() == "help":
            help_menu()


def title_screen():
    # Clears the terminal of prior code for a properly formatted title screen.
    os.system('clear')  # 'cls' for windows
    # Prints the pretty title.
    print('#' * 45)
    print('# Welcome to this text-based puzzle RPG for #')
    print("#      Bryan Tong's CS10 Final Project!     #")
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    title_screen_options()


#############
# Help Menu #
#############
def help_menu():
    print("")
    print('#' * 45)
    print("Written by ")
    print("~" * 45)
    print("Please ensure to type in lowercase for ease.\n")
    print('#' * 45)
    print("\n")
    print('#' * 45)
    print("    Please select an option to continue.     ")
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    title_screen_options()


#################
# Game Handling #
#################
quitgame = 'quit'


################
# Text Animation #
################
def typewriter(i):
    for char in i:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.1)
        else:
            time.sleep(1)


################
# Execute Game #
################
def setup_game():
    # Clears the terminal for the game to start.
    os.system('clear')  # 'cls' for windows

    # Establishes introduction
    message = "The lights flicker\n\
The curtains rise on your legend\n\
I wonder what role you will play?\n\
No matter.\n\
The only important thing now is...\n\
...your name\n"

    typewriter(message)

    # QUESTION NAME: Obtains the player's name.
    question1 = "Enter your name here: "
    typewriter(question1)
    player_name = input(" ")
    player1.name = player_name

    message1 = player1.name + "? Why does it sound familiar....\n\
Now...\n\
Your world...\n"

    typewriter(message1)

    # QUESTION MEMORIES: Obtains the player's memories.
    question2 = "Do you remember it?\n"
    typewriter(question2)
    memories = input("> ")
    player1.memories = memories.lower()

    # Creates the adjective vocabulary for the player's memories.
    yes_memories = ['y', 'yes', 'yah', 'yup']
    no_memories = ['idk', 'n', 'no', 'nah']

    # Identifies what type of memories the player is having and gives a related-sounding string.
    if player1.memories in yes_memories:
        memories_string = "Good. That'll make it easier for me."
    elif player1.memories in no_memories:
        memories_string = "No? Hehehe. You really are troublesome right up to the very end, aren't you?\n"
        typewriter(memories_string)
    else:
        memories_string = "As I suspected... You don't seem to be the true owner of this story. Goodbye."
        typewriter("Well then, " + player1.name + ", " + memories_string + ".")
        quit()

    while memories.lower() in no_memories:
        typewriter("Do you even want to remember?\n")
        memories = input("> ")
        player1.memories = memories.lower()

        if player1.memories in yes_memories:
            memories_string = "Good. That'll make it easier for me."
        elif player1.memories in no_memories:
            memories_string = "As if I care. I have a job to do y'know? It'll all come to you soon."
            typewriter("Well then, " + player1.name + ", " + memories_string + ".")
            quit()
        else:
            memories_string = "As I suspected... You don't seem to be the true owner of this story. Goodbye."
            typewriter("Well then, " + player1.name + ", " + memories_string + ".")
            quit()

    # Combines all the above parts.
    question3 = "Well then, " + player1.name + ", " + memories_string + ".\n"
    typewriter(question3)
    time.sleep(2)

    os.system('clear')
    # REALIZATION

    message2 = "As per 死神 and librarian guidelines, I will help you remember your story.\n\
Firstly, I need you to remember who you were.\n"

    typewriter(message2)
    time.sleep(1)

    # QUESTION AGE: Obtains the player's age.
    question4 = "Young, Adult, or Elderly?\n"
    typewriter(question4)
    age = input("> ")

    acceptable_age = ['young', 'adult', 'elderly']
    # Forces the player to write an acceptable age.

    while age.lower() not in acceptable_age:
        print("That is not an acceptable sign, please try again.")
        age = input("> ")
    player1.age = age.lower()

    if player1.age == 'young':
        age_string = "Ah... whether you were fortunate or not... To know this story came from a child... I'm sorry"
    elif player1.age == 'adult':
        age_string = "So your story began at the height of your life? How lucky of you"
    elif player1.age == 'elderly':
        age_string = "Fate chose you, regardless of age. Your strength might have waned but your wisdom was greater than ever"

    question5 = age_string + ".\n"
    typewriter(question5)
    time.sleep(2)
    playerorigin()


def playerorigin():
    message3 = "Now, do you remember where you came from?\n\
According to our data, there are only three settlements you could've possibly hailed from.\n\
Was it Riverrun? A quaint and homely town; far from conflict and disaster with kind and happy folks.\n\
Was it Aega? A citadel city, standing between order and chaos. Its citizens are hardy and courageous.\n\
Hm...\n\
Ah!\n\
Apologies, I had almost forgotten about Lunaly. That hidden settlement deep in the Aelvic woods.\n\
I've heard that its citizens are wise and knowledgeable beyond their years.\n\
Could it be an academic's paradise?\n\
Now, pray tell where you hailed from.\n"

    typewriter(message3)
    time.sleep(2)

    # QUESTION ORGIN: Obtains the player's origin.
    question6 = "Riverrun? Aega? Lunaly? or could you possibly hail from... nowhere?"
    typewriter(question6)

    origin = input("> ")
    acceptable_origin = ['riverrun', 'aega', 'lunaly', 'nowhere']
    # Forces the player to write an acceptable age.

    while origin.lower() not in acceptable_origin:
        print("That is not an acceptable origin, please try again.")
        origin = input("> ")
    player1.origin = origin.lower()

    if player1.origin == 'riverrun':
        origin_string = "Riverrun? How envious. Everyone else I've talked to so far came far more troubled backgrounds."
    elif player1.origin == 'aega':
        origin_string = "I see. Born in the face of adversity and chaos. You must be strong..."
    elif player1.origin == 'lunaly':
        origin_string = "Oh! I haven't met someone from there for quite some time. The last one was 200 years ago... Anyways."
    elif player1.origin == 'nowhere':
        # IF PLAYER INPUT NOWHERE
        speech1 = "...I...\n"
        speech2 = "...Let's move on.\n"
        origin_string = "Ah... A fellow orphan...? I understand your plight all too well.\n" + speech1 + speech2

    question7 = origin_string + ".\n"
    typewriter(question7)
    time.sleep(2)

    os.system('clear')
    goodbye()


def goodbye():
    message4 = "It seems we are finished.\n\
For the sake of guidelines, I must ask you to repeat what you have said to me\n\
I will repeat what you have told me.\n\
You are " + player1.name + ", " + player1.age + ", " + player1.origin + ".\n\
I thank you for your cooperation.\n\
May you find you worth, in the last reenactment of your story.\n"

    typewriter(message4)
    time.sleep(2)


title_screen()
