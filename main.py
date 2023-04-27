# Rock Paper Scissors Game
# ---------------------------------
# Start of the game:
# ---------------------------------
print("*"*40)
print("Welcome To Rock,Paper & Scissors Game!")
print("*"*40)
print("Rules:")
print("Rock beats scissors.")
print("Scissors beats paper.")
print("Paper beats rock.")
print("*"*40)
print("Choose one of the following:")
print("'Rock, Paper or Scissors'")
print("*"*40)
print("Then press enter to start the game.")
print("*"*40)
user_choice = input("Your choice: ")

if len(user_choice) == 0:
    print("You did not enter anything.")
    print("Please try again")
    exit()

# ---------------------------------
import random
random_number = random.randint(1,3)
# Random number assigned to computer_choice
# ---------------------------------
computer_choice = random_number
# ---------------------------------

# Rock, paper or scissors ASCII art
# ---------------------------------

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# ---------------------------------
Paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
# ---------------------------------
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""   
# ---------------------------------

# Player 1: user_choice

print("*"*40)
print("You:")
if user_choice == "Rock":
    print(Rock)
elif user_choice == "Paper":
    print(Paper)
elif user_choice == "Scissors":
    print(Scissors)
print("*"*40)    
# else:
#     print("You did not enter a valid choice.")
#     print("Please try again")
#     exit()
# ---------------------------------
# Player 2: computer_choice
print("Computer:")
if computer_choice == 1:
    computer_choice = "Rock"
    print(Rock)
elif computer_choice == 2:
    computer_choice = "Paper"
    print(Paper)
elif computer_choice == 3:
    computer_choice = "Scissors"
    print(Scissors)

# ---------------------------------
# Player 2 result:
if user_choice:
    print("*"*40)
    # print("Computer choose:")
#     print(computer_choice)
# ---------------------------------
#  Results Legend:
if user_choice == computer_choice:
    print("IT'S A TIE")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("YOU WIN!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("YOU WIN!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("YOU WIN!")
else:
    print("YOU LOSE!")
print("*"*40)
exit()
# ---------------------------------