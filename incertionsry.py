num=[1,9,2,8,3,7,4,7,5,6]
for i in range(len(num)):
    key=num[i]
    n=i-1
    while key<num[n] and n>=0:
        num[n+1]=num[n]
        n-=1
    num[n+1]=key

    print(num)