import random
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

def rock_scissor():
    print("Rock Paper Scissor Game")
    print("Rules:\nRock Beat Scissor\nScissor beat Paper\nPaper beat Rock")
    prin_choice=[rock,paper,scissors]
    ran=random.randint(0,2)
    computer_choice=prin_choice[ran]
    comp_no=ran
    user_guess=int(input("Enter 0 for Rock\nEnter 1 for Paper\nEnter 2 for Scissor?\n"))
    print(f"Your choice {prin_choice[user_guess]}")
    print(f"Computer choice= {computer_choice}")

    if user_guess==comp_no:
        print('Draw Game')
    elif user_guess==0 and comp_no==1:
        print("You Lose Paper beat Rock")
    elif user_guess==1 and comp_no==0:
        print("You Won")
    elif user_guess==1 and comp_no==2:
        print("You Lose Scissor beat Paper")
    elif user_guess==2 and comp_no==1:
        print("You winnnn")
    elif user_guess==0 and comp_no==2:
        print("You won ")
    elif user_guess==2 and comp_no==0:
        print("You Lose bcz Rock beat Scissor")


while True:
    rock_scissor()
    play_again = input("Do you want to play again y/n?\n")
    if play_again == 'y':
        print("\n"*20)
    else:
        break

