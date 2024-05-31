#unsort=[8,7,4,9,2,6,1,5]
unsort=["hi","bye","hello","goodbye"]
for u in range(len(unsort),):
    swap=False
    print("pass",u+1)
    for n in range(len(unsort)-1):
        if unsort[n] >= unsort[n+1]:
                temp=unsort[n]
                unsort[n]=unsort[n+1]
                unsort[n+1]=temp
                swap=True
        print(unsort)       
    if swap==False:
         break
   # print(unsort)