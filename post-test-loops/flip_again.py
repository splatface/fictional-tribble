import random


# again = "y" ---> line is no longer needed as it asks input later and is not a condition for the loop to run the first time

while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ")

    if again == "n":
        break