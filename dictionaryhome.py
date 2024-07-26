countrycapital={"india":"new delhi","luxebourg":"luxembourg city"}
while True:
    cc=int(input("1=add country and a capital \n2=remove country and a capital\n3=display countrys\n4=display all capitals\nelse end program"))

    if cc==1:
        count=input("what country")
        capit=input("what capital")
        countrycapital[count]=capit
        print(countrycapital)

    elif cc==2:
        which=input("which country")
        del countrycapital[which]
        print(countrycapital)

    elif cc==3:
        print(countrycapital.keys())

    elif cc==4:
        print(countrycapital.values())
    
    else:
        break