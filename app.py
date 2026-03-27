"""Rock, Paper, Scissors game """
import random
options = ("r", "p", "s")
wining_comp = (("r", "s"), ("p", "r"), ("s", "p"))
emojis = {"r":"🪨", "p":"📰", "s":"✂️"}

def print_choces():
    print("----------------------------")
    print(f"you chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")
    print("----------------------------")

while True:
    user_choice = input("Rock, Paper or scissors (R/P/S) / Q to quit: ")
    computer_choice = random.choice(options)

    if user_choice.lower() == "q":
        break
    elif user_choice.lower() not in options:
        print("Enter a valid option (R, P, or S)")
        print("_____________________________________")
        print()
        continue
    elif user_choice == computer_choice:
        print_choces()
        print("It's a tie!")
        print("_____________________________________")
        print()
    elif (user_choice, computer_choice) in wining_comp:
        print_choces()
        print("You won!")
        print("_____________________________________")
        print()
    else:
        print_choces()
        print("Computer won!")
        print("_____________________________________")
        print()