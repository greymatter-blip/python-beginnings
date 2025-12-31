# a code to roll 2 dices and generate their values 
import random
def roll():
    x = random.randint(1,6)
    y = random.randint(1, 6)
    return x,y

command = ""
while command != "n":
    command = input("Roll the dice? (y/n): ").lower()
    if command == "y":
        print(roll())
    elif command == "n":
        break
    else:
        print("Invalid Input")
