"""Rock, Paper, Scissors game """
import random
options = ["Rock", "Paper", "Scissors"]

user_choice = input("Rock, Paper or scissors (R/P/S):")
computer_choice = random.choice(options)
