import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

###### Player Setup ######
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
myPlayer = player()

###### Title Screen ######
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        optio = input("> ")
        if option.lower() == ("play"):
            start_game() #placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    # Clears the terminal of prior code for a properly formatted title screen.
    os.system('clear')
    # Prints the pretty title.
    print('#' * 45)
    print('# Welcome to this text-based puzzle RPG for #')
    print("#      Bryan Tong's CS10 Final Project!     #")
    print('#' * 45)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    title_screen_selections()

def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('Use up, down, left, right to move')
    print('Type your commands to do them')
    print('Use "look" to inspect something')
    print('Good luck and have fun!')
    title_screen_selections()

##### GAME FUNCTIONALITY ######
def start_game():
