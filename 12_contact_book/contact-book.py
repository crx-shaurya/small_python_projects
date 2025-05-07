contacts= {
    "dhruv" : 9411062269,
    "mummy" : 7887036277,
    "papa" : 9935406277
}
print(contacts(1))
def see_contact(name):
    if name in contacts:
        print(name, contacts[name])
    elif name not in contacts:
        print("contact not found")
        b = input("do you want to add it y/n: ")
        if b == "y" or b == "yes":
            add_contact(name)
        elif b == "n" or b == "no":
            print("ok, no worries")
        else:
            print("sorry! \ninvalid input")
    else:
        print("sorry!, invalid input")

def add_contact(name):
    c = int(input(f"please enter the mobile number of {name}: "))
    contacts[name] = c
    print("contact added successfully")

def show_all_contacts():
    for i in range(len(contacts)):
        print(contacts[i])

a = input("what do you want to do add or see contact or exit, ")
if a == "add" or a == "Add":
        e = input("enter the name of contact, ")
        add_contact(e)
elif a == "see" or a == "See":
    f = input("do you want to see all contacts or a particular one a/p: ")
    if f == "all" or a == "a" or a == "All":
        show_all_contacts()
    elif f == "p" or f == "P" or f == "particular":
        d = input("enter the name of contact, ")
        see_contact(d)
elif a == "exit" or a == "Exit":
    print("ok, bye!")
    exit()
else:
    print("invalid input")    

   
