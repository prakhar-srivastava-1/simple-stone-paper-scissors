rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# import random module for Computer's choice
import random

# Put all the choices in a list
choices = [rock, paper, scissors]

# take input from the user
user_choice = int(input("Please enter your choice. 0 for Rock, 1 for Paper and 2 for Scissors: "))

# Generate a random choice for computer
computer_choice = random.randint(0,2)

# Check if User has input a valid number
if user_choice in [0, 1, 2]:
  print("You chose:")
  print(choices[user_choice] + "\n")
  print("Computer chose:")
  print(choices[computer_choice] + "\n")

  # Create the result map
  # User wins (0, 2); (1, 0); (2, 1)
  # User loses (2, 0); (0, 1); (1, 2)
  # Draw (0, 0); (1, 1); (2, 2)
  result_map = [
    ["DRAW", "LOST", "WON"],
    ["WON", "DRAW", "LOST"],
    ["LOST", "WON", "DRAW"]
    ]

  # Print the result
  # If the choices are same -> DRAW: Diagonal elements
  if(user_choice == computer_choice):
    print("It's a DRAW!")
  else:
    print("You " + result_map[user_choice][computer_choice])

# Handle invalid input
else: print("Invalid choice; You LOST!")

input("Press any key to exit")
