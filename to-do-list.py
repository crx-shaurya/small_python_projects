# To-Do List Application

def edits():

    with open("tasks.txt", "r") as f:
        tasks = f.read()

        print("1. Add a task \n2. finish a task \n3. show all tasks \n4. exit")
        a=int(input("what do you want to do: "))

        if a ==1:
            b= input("enter the new task, ")

            if b not in tasks:
                with open("tasks.txt", "a") as g:
                    g.write(b + "\n")
                print("task added")
                edits()

            elif b in f:
                print("task already there")
                edits()

            else:
                print("enter valid input")
                edits()

        elif a == 2:
            print(tasks)
            c=input("enter the task you finishes:")
            if c in tasks:
                with open("tasks.txt", "w") as i:
                    tasks = tasks.replace(c, "")
                    i.write(tasks)
                print("task finished")
                edits()
            
            elif c not in tasks:
                print("task not found")
                edits()
            
            else:
                print("invalid input")
                edits()

        elif a == 3:

            if len(tasks) == 0:
                print("no tasks to show")
                edits()

            else:
                print(tasks)
                edits()
        
        elif a == 4:
            exit()

        else:
            print("invalid input")
            edits()

edits()

# print(tasks)