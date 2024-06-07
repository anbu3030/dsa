#Function to print the numbers from 1 to n.
def f1n(num):
    for n in range(1,num+1):
        print(n)
f1n(10)
"""print(round(22/7,1000000000000))"""

#Function that displays the multiplication table of a number

def mtn(sn):
    for i in range(11):
        print(sn*i)
inp=int(input("1.display number\n 2.multiplication\n select an option:"))
if inp==1:
    inpp=int(input("which number to display"))
    f1n(inpp)

else:
    number=int(input("which number"))
    mtn(number)