is_game_cont=True
def treasue_island():
    print("Welcome to Treasue Island")
    print("Your mission is to find the treasure")
    input01 = input("You are at the cross road where you want to go?\nType 'left' or 'right' ")
    if input01 == 'right':
        print('Fall into a Hole. Game Over !')
    elif input01 == 'left':
        print("You have come to lake. There is a island in the middle of the lake.")
        input02 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
        if input02 == 'swim':
            print("Attacked by Trout. Game Over")
        elif input02 == 'wait':
            print("You arrive at the island unharmed. There is a house with 3 doors")
            input03 = input("One red, One yellow and One blue. Which colour do you choose?\n")
            if input03 == "red":
                print("Burned by a Fire! GameOver")
            elif input03 == "blue":
                print("Eaten by beast Game Over!")
            elif input03 == 'yellow':
                print("You Win !!!!!")
            else:
                print("Game Over")
while is_game_cont:
    treasue_island()
    want_play=input("Do you want to play again y/n?\n")
    if want_play=='y':
        print('\n'*20)
        is_game_cont=True
    else:
        is_game_cont=False