# game.py

import os
from dotenv import load_dotenv
load_dotenv()
USER_NAME = os.getenv("USER_NAME", default="Player One")
import random

print ("Hello and welcome to the game. Strap in and hang on tight", USER_NAME)

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

#print(user_choice)
print("USER CHOICE: ", user_choice)


#vaildate the input such tthat only if it is one of the expected values
#...will we continue with the rest of the program
#...otherwise we'll stop the program before eit tries to do anything else
#...and we'll ask the user to run the program again

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("You chose:", user_choice)
else:
    print("OOPS, invalid input. Please try again.")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("The computer chose:", computer_choice)

if user_choice == computer_choice:
    print ("It's a tie! Play again.")
elif (user_choice == "rock") and (computer_choice == "scissors" ):  
    print("Yay! You won!")
elif(user_choice == "rock") and (computer_choice == "paper"):
    print("Oh no, you lost this round.")
elif (user_choice == "paper") and (computer_choice == "scissors"):
    print ("You lost. Bummer. Try again.")
elif (user_choice == "paper") and (computer_choice == "rock"):
    print ("Hey! You won! Congrats!")
elif (user_choice == "scissors") and (computer_choice == "rock"):
    print ("SMASHED! Sorry, you lose. Try again.")
elif (user_choice == "scissors") and (computer_choice == "paper"):
    print ("Wahoo! Shredded the competition ;)")

print ("The game is over. Thanks for playing!")