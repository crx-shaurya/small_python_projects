
# quiz game with score tracking

questions = ["What is the capital of France?","What is 2 + 2?","Who wrote 'Hamlet'?","What is the largest planet in our solar system?","What is the boiling point of water in Celsius?","Who painted the Mona Lisa?","What is the smallest prime number?","What is the chemical symbol for gold?","What is the square root of 64?","Who discovered gravity?"]
answers = ["a) Paris\n b) London\n c) Berlin\n d) Madrid\n", "a) 3\n b) 4\n c) 5\n d) 6\n", "a) Charles Dickens\n b) William Shakespeare\n c) Mark Twain\n d) Jane Austen\n", "a) Earth\n b) Mars\n c) Jupiter\n d) Saturn\n", "a) 90°C\n b) 100°C\n c) 110°C\n d) 120°C\n","a) Vincent van Gogh\n b) Pablo Picasso\n c) Leonardo da Vinci\n d) Claude Monet\n", "a) 0\n b) 1\n c) 2\n d) 3\n","a) Au\n b) Ag\n c) Fe\n d) Hg\n","a) 6\n b) 7\n c) 8\n d) 9\n","a) Isaac Newton\n b) Albert Einstein\n c) Galileo Galilei\n d) Nikola Tesla\n"]

def play():
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        print(answers[i])
        answer = input("please enter your answer, ")
        if answer == "a" or answer == "A":
            score += 1
            print("correct")
        elif answer == "b" or answer == "B":
            score += 2
            print("correct")
        elif answer == "c" or answer == "C":
            score += 3
            print("correct")
        elif answer == "d" or answer == "D":
            score += 4
            print("correct")
        else:
            print("wrong")
    print(f"your total score is {score}")


name = input("please enter your name, ")
print(f"hi {name}")
print("welcome to the quiz game")
print("rules are simple")
print("You will be asked 10 questions")
print("choose the correct option and get points")
print("choose 1 for a, 2 for b, 3 for c, 4 for d")
print("let's start the game")
print(f"good luck {name}")

play()
