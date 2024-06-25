# Asks for Origin of the PMC (Player Main Character)
def characreateorigin():
    places = [("Now, do you remember where you came from?", 2),
              ("According to our data, there are only three settlements you could've possibly hailed from.", 2),
              ("Was it Riverrun? A quaint and homely town; far from conflict and disaster with kind and happy folks.",
               3),
              ("Was it Aega? A citadel city, standing between order and chaos. Its citizens are hardy and courageous.",
               3),
              ("Hm...", 2),
              ("Ah!", 1),
              ("Apologies, I had almost forgotten about Lunaly. That hidden settlement deep in the Aelvic woods.", 2),
              ("I've heard that its citizens are wise and knowledgeable beyond their years.", 1),
              ("Could it be an academic's paradise?", 1),
              ("Now, pray tell where you hailed from.", 2)]
    for place, delay in places:
        print(place)
        sleep(delay)
    choices = [("riverrun", 2),
               ("aega", 2),
               ("lunaly", 2),
               ("nowhere", 2)]
    player_origin_choice = input("Riverrun? Aega? Lunaly? or could you possibly hail from... nowhere?").lower()
    if player_origin_choice in [choice[0] for choice in choices]:
        if player_origin_choice == "riverrun":
            print("Riverrun? How envious. Everyone else I've talked to so far came far more troubled backgrounds.")
        elif player_origin_choice == "aega":
            print("I see. Born in the face of adversity and chaos. You must be strong...")
        elif player_origin_choice == "lunaly":
            print(
                "Oh! I haven't met someone from there for quite some time. The last one was 200 years ago... Anyways.")
        elif player_origin_choice == "nowhere":
            print("Ah... A fellow orphan...? I understand your plight all too well.")
            sleep(2)
            print("...I...")
            sleep(2)
            print("...Let's move on.")
            sleep(1)
    else:
        print("As I suspected... You don't seem to be the true owner of this story. Goodbye.")
        quit()

