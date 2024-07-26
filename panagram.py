#while True:
pan=input("enter a number")
pool=["0","1","2","3","4","5","6","7","8","9"]
for p in pan:
    if p in pool:
        pool.remove(p)
print(pool)
if len(pool)==0:
    print("this is a panagram")
else:
    print("this is not a panogram")