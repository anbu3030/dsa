#Print the odd numbers from 1 till the number entered by the user.

entery=int(input("enter up to which number you want"))
odd=1

for o in range(1,entery+1,2):
    print(o)


print("question number 2")


#Print the numbers starting with the number of user's choice till 1.

for e in range(entery,0,-1):
    print(e)

print("question number 3")
#Print the even numbers from 1 till the number entered by the user.

for l in range(0,entery+1,2):
    print(l)
print("question number 4")
#Print a multiplication table of a number for the first 10 multiples.


for x in range(entery,10*entery+1,entery):
    print(x)
