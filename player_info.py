# Asks for Player Info
def characreateinfo():
    realization = [("As per 死神 and librarian guidelines, I will help you remember your story.", 2),
                   ("Firstly, I need you to remember who you were.", 2)]
    for realization, delay in realization:
        print(realization)
        sleep(delay)
    player_age_choice = input("Young, Adult, or Elderly?").lower()
    if player_age_choice == 'young':
        print("Ah... whether you were fortunate or not... To know this story came from a child... I'm sorry.")
    elif player_age_choice == 'adult':
        print("So your story began at the height of your life? How lucky of you.")
    elif player_age_choice == 'elderly':
        print("Fate chose you, regardless of age. Your strength might have waned but your wisdom was greater than ever")
    else:
        print("As I suspected... You don't seem to be the true owner of this story. Goodbye.")
        quit()
    sleep(2)
