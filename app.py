"""Rock, Paper, Scissors game """
import random
options = ["r", "p", "s"]



while True:
    user_choice = input("Rock, Paper or scissors (R/P/S) / Q to quit: ")
    computer_choice = random.choice(options)

    if user_choice.lower() == "q":
        break
    elif user_choice.lower() not in options:
        print("Enter a valid option (R, P, or S)")
        continue
    elif user_choice == computer_choice:
        print(f"you chose: {user_choice}, Computer chose: {computer_choice}")
        print("It's a tie!")
    elif (user_choice == "r" and computer_choice == "s" or
         user_choice == "p" and computer_choice == "r" or
         user_choice == "s" and computer_choice == "p"):
         print(f"you chose: {user_choice}, Computer chose: {computer_choice}")
         print("You won!")
    else:
        print(f"you chose: {user_choice}, Computer chose: {computer_choice}")
        print("Computer won!")