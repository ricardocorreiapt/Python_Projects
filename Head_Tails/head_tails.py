import random

num = random.randint(1,2)
guess = None

while guess != num:
    guess = input("1 for Head or 2 for Tails: ")
    guess = int(guess)

    if guess == num:
        print("You won!!! ")
        if guess == 1:
            print("Heads")
        else:
            print("Tails")

        break
    else:
        print("Wrong Try Again")

