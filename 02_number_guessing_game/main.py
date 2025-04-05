import random

guess = random.randint(1,100)
attempts = 1
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100. Can you guess it?")
print("You have 5 attempts to guess the number. Good luck!")
while attempts < 6:
    try:
        user=int(input("enter your guess, "))
        if user==guess:
            print("Congratulations! You guessed the number!")
            break
        else:
            print("ouch! Wrong guess.")
            print(f"now you have {5-attempts} attempts left.")
            attempts+=1

    except:
        print("something went wrong")
        a=input("do you want to continue? (yes/no), ")
        if a=="yes" or a=="y":
            continue
        else:
            print("thanks for playing")
            break
