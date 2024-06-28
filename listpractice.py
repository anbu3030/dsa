#Write a program to find the sum of items in a list.

num=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
sum=0
for n in range(len(num)):
    sum+=num[n]

print(sum)

#Write a Python program to get the largest number from a list.

big=0
for n in range(len(num)):
    if big<num[n]:
        big=num[n]
print(big)

#from a list create a new list by removing duplicates.
new=[]
for n in range(len(num)):
    if num[n] not in new:
        new.append(num[n])
print(new)