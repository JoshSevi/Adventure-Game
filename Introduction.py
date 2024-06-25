from time import sleep


# Establishes introduction
def openingscene():
    messages = [("The lights flicker", 2),
                ("The curtains rise on your legend", 2),
                ("I wonder what role you will play?", 2),
                ("No matter.", 2),
                ("The only important thing now is...", 2),
                ("...your name", 2)]
    for message, delay in messages:
        print(message)
        sleep(delay)

    ininame = input("Enter your name here:")

    messages2 = [(ininame + "? Why does it sound familiar....", 2),
                 ("Now... Your world... Do you remember it?", 2)]
    for messages2, delay in messages2:
        print(messages2)
        sleep(delay)

    memories = input("Y/N?").lower()
    if memories == 'y':
        print("Good. That'll make it easier for me.")
    elif memories == 'n':
        print("No? Heheh. You really are troublesome right up to the very end, aren't you?")
        remember = input("Do you even want to remember?").lower()
        if remember == 'yes' or remember == 'y':
            print("Then let me tell you about yourself...")
        elif remember == 'no' or remember == 'n':
            print("As if I care. I have a job to do y'know? It'll all come to you soon.")
    else:
        print("As I suspected... You don't seem to be the true owner of this story. Goodbye.")
        quit()
    sleep(2)

