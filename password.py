password={"hi":"bye","hello":"goodbye","number":"123456"}

user=input("enter username ")

if user in password:
    passcode=input("enter password ")

    if passcode==password[user]:
        print("you are loged into the system")

    else:
        print("passcode in invalid")

else:
    print("username incorrect")