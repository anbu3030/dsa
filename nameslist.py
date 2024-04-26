names=["hi","bye"]
while True:
    print("1.Add a name\n 2. Change a name\n 3.Delete a name\n 4.View all names\n 5. exit")
    option=input("select an option:")
    if option==str(1):
        add=input("what are you adding: ")
        names.append(add)
        print(names)

    elif option==str(2):
        change=input("which value are you changing: ")
        if change not in names:
            print("not in the list")
        else:
            new=input("what is the new name: ")
            names[names.index(change)]=new
            print(names)

    elif option==str(3):
        remove=input("what are you removing: ")
        if remove not in names:
            print("not in list")
        else:    
            names.remove(remove)
            print(names)

    elif option==str(4):
        for d in names:
            print(d)
    
    elif option==str(5):
        break



