from sys import exit
dead = False


def mountain():
    print("Head west toward the mountains. It begins to snow, what do you do?")
    print("Build a shelter, or do nothing?")
    next_try = input("> ")

    if "shelter" in next_try:
        print("You start to build shelter, but it starts to sleet.")

    elif "nothing" in next_try:
        print("Why stop? You're not afraid of a little cold.")
        print("You get frost bite, and freeze to death. Congrats!")
        redo = input("Would you like to play again? ")
        if "Y" in redo or "y" in redo:
            start()
        else:
            exit(0)


def woods():
    print("You start climbing north. The woods are getting thick.")
    print("You find an abandoned cabin. What do you do?")
    print("1. Try the front door \n2. Check the window.")

    next = input("> ")
    if "front" in next or "1" in next:
        print("You enter the cabin through the front door and are shot on sight.")
        print("Death can be bitter sweet sometimes!")
        redo = input("Would you like to play again? ")
        if "Y" in redo or "y" in redo:
            start()
        else:
            exit(0)
    elif "Check" in next or "2" in next:
        print("You see someone through the window, he doesn't look friendly.")
        print("Good instincts! What do you want to do next?")
        print("1. Enter the cabin through the back window. \n2. Throw a knife through the window. \n3. Don't risk it.")
    else:
        print("Invalid input. Try again.")
        woods()

    next_try = input("> ")
    if "enter" in next_try or "1" in next_try:
        print("You manage to subdue him and keep warm for the night! Congrats!")
        print("You thought you were safe, he escapes his bonds and eats you.")
        redo = input("Would you like to play again? ")
        if "Y" in redo or "y" in redo:
            start()
        else:
            exit(0)
    elif "knife" in next_try or "2" in next_try:
        print("You hit him with the knife in the throat.")
        print("You scored a place to live and decide to live off the land!")
        print("If you're under 22, you didn't survive longer than three days without TV.")
        redo = input("Would you like to play again? ")
        if "Y" in redo or "y" in redo:
            start()
        else:
            exit(0)
    elif "don't" in next_try or "3" in next_try:
        print("You chose to be indecisive and froze to death! \nSometimes death can be the easier way out.")
        redo = input("Would you like to play again? ")
        if "Y" in redo or "y" in redo:
            start()
        else:
            exit(0)
    else:
        print("Invalid input! \nTry again!")
        woods()

def shore():
    print("You chose the fastest route of escape, fastest isn't always the easiest.")
    print("You begin to walk down the shore line. It's getting dark.")
    print("You see a group of natives up ahead. Should you approach them?")
    next = input("> ")

    if "no" in next:
        print("Correct! Trust no one. You chose to follow the tree line. Narrowly escaping death.")
        print("You see a boat, do you want to chance it? It seems a bit small..")
        next_try = input("> ")

        if "no" in next_try:
            print("You chose to be indecisive, waiting at the shore forever.")
            print("You pace around slowly until the sun takes your life.")
            redo = input("Would you like to play again? ")
            if "Y" in redo or "y" in redo:
                start()
            else:
                exit(0)
        if "yes" in next_try:
            print("You manage to fight the rip current.")
            print("The waves start to swell, you always knew 'The Titanic' was a lie!")
            print("The boat quickly starts to take on water. It sinks and you can't swim!")
            redo = input("Would you like to play again? ")
            if "Y" in redo or "y" in redo:
                start()
            else:
                exit(0)
    if "yes" in next or "approach" in next:
        print("They seem friendly enough. They give you food and shelter.")
        print("You fall asleep staring into the fire.")
        print("You are awoken by the feeling of tight ropes around your arms.")
        print("They decide to cook you alive! Cannibals, huh? \nCan't live with them and they enjoy how you taste.")


def start():
    print("You decided to go on a cruise in the pacific.")
    print("Off the coast of California, the boat catches fire.")
    print("All of the life boats have been taken, you decide to take a chest of drawers.")
    print("Since this isn't the Titanic, you don't freeze to death, you reach an island.")
    print("You have three options: ")
    print("1. Head West along the shoreline. 2. Head North up the mountain. 3. Go East through the woods.")

    next = input("> ")

    if next == "1" or "West" in next:
        shore()
    elif next == "2" or "North" in next:
        mountain()
    elif next == "3" or "East" in next:
        woods()
    else:
        print("You go nowhere, the search and rescue team finds you and you live!")
        print("Nice way to take the cheap way out!")
        redo = input("Would you like to play again? ")
        if "Y" in redo or "y" in redo:
            start()
        else:
            exit(0)


start()

