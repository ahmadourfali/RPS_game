"""Rock, Paper, Scissors game """
import random
options = ["r", "p", "s"]
wining_comp = [("r", "s"), ("p", "r"), ("s", "p")]

def print_choces():
    print(f"you chose: {user_choice}, Computer chose: {computer_choice}")

while True:
    user_choice = input("Rock, Paper or scissors (R/P/S) / Q to quit: ")
    computer_choice = random.choice(options)

    if user_choice.lower() == "q":
        break
    elif user_choice.lower() not in options:
        print("Enter a valid option (R, P, or S)")
        continue
    elif user_choice == computer_choice:
        print_choces()
        print("It's a tie!")
    elif (user_choice, computer_choice) in wining_comp:
        print_choces()
        print("You won!")
    else:
        print_choces()
        print("Computer won!")