"""Rock, Paper, Scissors game """
import random
options = ["r", "p", "s"]



while True:
    user_choice = input("Rock, Paper or scissors (R/P/S):")
    computer_choice = random.choice(options)

    if user_choice.lower() not in options:
        print("Enter a valid option (R, P, or S)")
        
    elif user_choice == computer_choice:
        print("It's a tie!")
        break
    else:
        print(f"you chose: {user_choice}, Computer chose: {computer_choice}")