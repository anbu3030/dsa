unsort=[8,7,4,9,2,6,1,5]

for n in range(len(unsort),):
    swap=False
    print("pass",n+1)
    for u in range(len(unsort)-1):
        if unsort[u] < unsort[u+1]:
                temp=unsort[u]
                unsort[u]=unsort[u+1]
                unsort[u+1]=temp
                swap=True
        print(unsort)       
    if swap==False:
         break
    
print (" this is insertion sort")


num1=[1,9,2,8,3,7,4,7,5,6]
for i in range(len(num1)):
    key=num1[i]
    n1=i-1
    while key>num1[n1] and n1>=0:
        num1[n1+1]=num1[n1]
        n1-=1
    num1[n1+1]=key

    print(num1)