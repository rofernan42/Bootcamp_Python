from random import randint

guess = randint(1, 99)
tries = 0
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

while 1:
    print("What's your guess between 1 and 99?")
    tries += 1
    try:
        nb = input(">> ")
        if nb == "exit":
            exit("You have left the game.")
        nb = int(nb)
        if nb == guess:
            print("Congratulations, you've got it!")
            if guess == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if tries == 1:
                exit("Well done, you found at the first attempt!")
            else:
                exit("You won in " + str(tries) + " attempts!")
        elif nb < guess:
            print("Too low!")
        elif nb > guess:
            print("Too high!")
    except ValueError:
        print("That's not a number.")