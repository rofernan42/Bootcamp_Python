import random
import sys

nbr = random.randint(1, 99)
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.\nGood luck!\n")
att = 0
while 1:
    try:
        choice = input("What's your guess between 1 and 99?\n")
        if choice == "exit":
            sys.exit("Exit game")
        choice = int(choice)
        if choice > nbr:
            print("Too high!")
            att += 1
        elif choice < nbr:
            print("Too low!")
            att += 1
        elif choice == nbr:
            print("Congratulations, you've got it!")
            att += 1
            if nbr == 42:
                print("Douglas Adams.")
            if att == 1:
                sys.exit("You found on the first try!")
            else:
                sys.exit("You won in %d attempts!" % att)
    except ValueError:
        print("That's not a number.")
        att += 1