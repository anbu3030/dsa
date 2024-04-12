class Car:
    
    shape="rectangle"
    wheel="4"

    def __init__(self,color,size):
        self.color=color
        self.size=size
        self.km=0

    def drive(self,distance):
        self.km+=distance

car1= Car("green",(700,600),)
print (car1.shape)
print (car1.color)
print (car1.size)
print (car1.wheel)
print (car1.km)
car1.drive(10)
print (car1.km)
car1.drive(100)
print (car1.km)

car2= Car("red",(750,750))
print (car2.shape)
print (car2.color)
print (car2.size)
print (car2.wheel)