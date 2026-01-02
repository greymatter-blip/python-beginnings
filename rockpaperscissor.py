#ask input from user
print("welcome to a game of rock, paper and scissors")

i = ""
while i != "n":
    choice = ("r" , "s" , "p")
    usr_choice = input("enter your choice: (r/p/s) ").lower()

    #if input is valid continue else print invalid input
    sign = {
        "r" : "🪨",
        "p" : "📃",
        "s" : "✂️"
    }
    if usr_choice in choice:
        print(f"you chose {sign.get(usr_choice, usr_choice)}")
    else:
        print("invalid input")
        break

    #let computer choose randomly
    import random
    comp_choice = random.choice(choice)
    print(f"computer chose {sign.get(comp_choice, comp_choice)}")

    #compare and display winner
    if comp_choice == usr_choice:
        print("it's a draw")
    elif (comp_choice == "r" and usr_choice == "s") or (comp_choice == "s" and usr_choice == "p") or (comp_choice == "p" and usr_choice == "r"):
        print('computer wins')

    elif (usr_choice == "r" and comp_choice == "s") or(usr_choice == "s" and comp_choice == "p") or (usr_choice == "p" and comp_choice == "r"):
        print("user wins")

    #ask if wanna play again
    i = input("do you want to play again? (y/n) ").lower()
