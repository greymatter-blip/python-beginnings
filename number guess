#this is a project to guess the number between 1 and 100

import random
sec = random.randint(1, 100)
guess = ""
i = 0
try:
    while guess != sec:
        guess = int(input("enter a number between 1 to 100: "))
        i += 1
        if guess > sec:
            print("guess too high!")
        elif guess < sec:
            print("guess too low!")
        elif guess == sec:
            print(f"congrats! you won in {i} tries")
except ValueError:
    print("invalid input")
