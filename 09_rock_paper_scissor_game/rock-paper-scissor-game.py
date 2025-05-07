import random

def play():

    a= int(input("Enter your choice: "))
    b = random.randint(1, 3)


    if b == 1:
        if a == 1:
            print("It's a Tie!")
            print("you both have choosen rock")
            play()
        elif a == 2:
            print("You Win!")
            print(f"you have choosen paper and computer has choosen rock")
            play()
        elif a == 3:
            print("You Lose!")
            print(f"you have choosen scissor and computer has choosen rock")
            play()
        elif a == 4:
            print("thanks for playing")
            exit()
        else:
            print("invalid choice")
            play()
    
    elif b == 2:
        if a == 1:
            print("You Lose!")
            print(f"you have choosen rock and computer has choosen paper")
            play()
        elif a == 2:
            print("It's a Tie!")
            print(f"you both have choosen paper")
            play()
        elif a == 3:
            print("You Win!")
            print(f"you have choosen scissor and computer has choosen paper")
            play()
        elif a == 4:
            print("thanks for playing")
            exit()

    elif b == 3:
        if a == 1:
            print("you win")
            print(f"you have choosen rock and computer has choosen scissor")
            play()
        elif a == 2:
            print("You Lose!")
            print(f"you have choosen paper and computer has choosen scissor")
            play()
        elif a == 3:
            print("It's a Tie!")
            print(f"you both have choosen scissor")
            play()
        elif a == 4:
            print("thanks for playing")
            exit()
        else:
            print("invalid choice")
            play()

def start():
    p = input("press enter to start the game")
    if p == "":
        play()
    elif p == "exit":
        exit()
    else:
        print("invalid choice")
        start()

print("Welcome to Rock, Paper, Scissors Game!")
print("choose numbers according to your choice")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Exit")
print("computer has choosen a option")

start()
