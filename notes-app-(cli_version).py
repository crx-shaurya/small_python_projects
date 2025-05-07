def write():
    note = input("enter your note here: ")
    with open("notes.txt", "a") as notes:
        notes.seek(0)
        p = notes.readlines()
        if note + "\n" not in p:
            notes.write(note + "\n")

def read():
    with open("notes.txt") as notes:
        a = notes.read()
        print(a)

input = input("what do you want to do, read/write: ")

if input.lower() == "read":
    read()
elif input.lower() == "write":
    write()