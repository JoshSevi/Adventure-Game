import sys
import os
from game import setup_game


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


title_screen()
