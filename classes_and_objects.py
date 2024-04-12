class Phone:
    #class variable
    shape="rectangle"

    #constructor
    #instance variables

    def __init__(self,color,size):
        self.color=color
        self.size=size

    def photo(self):
        print("saved to gallary")

phone1= Phone("teal",(500,600))
print (phone1.shape)
print (phone1.color)
print (phone1.size)
phone1.photo()

phone2= Phone("red",(650,750))
print (phone2.shape)
print (phone2.color)
print (phone2.size)