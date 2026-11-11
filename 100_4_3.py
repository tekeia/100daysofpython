import random

# User selection
selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Computer random selection
computer_selection = random.randint(0,2)

# Tools ASCCI
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
---'    ____)____
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

tools = [rock, paper, scissors]

if selection >= 0 and selection <= 2:
    if selection == 0:
        print(rock)
    elif selection == 1:
        print(paper)
    elif selection == 2:
        print(scissors)
        
    print(f"Computer chose:{tools[computer_selection]}")

    if selection == 0 or selection == 1 or selection == 2:
        if selection == computer_selection:
            print("Draw")
        elif computer_selection == 0 and selection == 1 or computer_selection == 1 and selection == 2 or computer_selection == 2 and selection == 0:
            print("You win")
        else: 
            print("You lose")  

else:
    print("You haven't made an acceptable selection.")