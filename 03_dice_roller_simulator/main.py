import random

def roll():
    number=random.randint(1,6)
    print("press enter to roll the dice or any other key to exit")
    a=input()
    if a == "":
        print(f"you rolled a, {number}")
    
    elif a != "":
        print("thanks for playing")
        exit()

while True:
    try:
        roll()
    except:
        break
