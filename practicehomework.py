#area and perimeter of a square
#area and perimeter of a rectangle
def square(v):
        
    print("area=",v*v)
    print("perimeter=",v+v+v+v)

def rectangle(v,rv):

    print("area=",v*rv)


    print("perimeter=",v+rv+v+rv)

def circle(r):
    print("area=",3.14*r*r)

    print("perimeter=",3.14*r*2)
while True:
    print("1=area and perimeter of square\n 2=area and perimater of rectangle\n3=area and circumference of circle\n 4=stop")
    inp=int(input("which funtion would you like to use"))
    if inp==1:
        squ=int(input("how big"))
        square(squ) 

    elif inp==2:
        squ=int(input("how big"))
        rec=int(input("how big is the long side"))
        rectangle(squ,rec) 

    elif inp==3:
        cir=int(input("how long is the radius"))
        circle(cir) 

    elif inp==4:
        break