
def fareheit():
    # convert fareheit to celies
    f=int(input("fareheit"))
    c=f-32
    sec=5/9
    cel=c*sec
    print(cel)

def hour():
    m=int(input("minutes"))
    h=m//60 
    min=m%60
    print("hour=",h,"\nminutes=",min)

def inches():
    i=int(input("inches"))
    cm=i*2.54
    print(cm)

while True:
    menu=int(input("menu\n1=fareheit to celies\n2=hours to minutes\n3=inches to cm\n4=end"))
    if menu==1:
        fareheit()
    elif menu==2:
        hour()
    elif menu==3:
        inches()
    else:
        break