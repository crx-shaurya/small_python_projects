#i will use functions for each operation.

def add():
    try:
        a=int(input("enter the first number, "))
        b=int(input("enter the second number, "))
        print(f"the sum of {a} and {b} is {a+b}")
    
    except:
        print("please enter valid number)")
        add()

def subtract ():
    try:
        a=int(input("enter the first number, "))
        b=int(input("enter the second number, "))
        print(f"the difference of {a} and {b} is {int(a)-int(b)}")
    
    except:
        print("please enter a valid number")
        subtract()
    
def multiply():
    try:
        a=int(input("enter the first number, "))
        b=int(input("enter the second number, "))
        print(f"the product of {a} and {b} is {a*b}")
    
    except:
        print("please enter valid number")
        multiply()

def divide():
    try:
        a=int(input("enter the first number, "))
        b=int(input("enter the second number, "))
        print(f"the quotient of {a} and {b} is {a/b}" if a%b == 0 else f"the quotient of {a} and {b} is {a//b} and the remainder is {a%b}")
    
    except:
        print("please enter valid number")
        divide()
    
p= input("enter the operation you want to perform, add, subtract, multiply, divide: ")
add() if p == "add" else subtract() if p == "subtract" else multiply() if p == "multiply" else divide() if p == "divide" else print("please enter a valid operation")
