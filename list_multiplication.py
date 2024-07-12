def multi(num):
    product=1
    for n in num:
        product*=n
    print(product)

multi([10,9,11,8,12])
multi([12,3,1,5,6,3])

def smallist(nu):
    value=nu[0]
    for n in nu:
        if value>n:
            value=n
    print(value)

smallist([10,9,1,2,8,7,3,4,6,5])
smallist([13,3,2,5,24,2,4,45,23,87,4])

for i in range(1,6):
    print(str(i)*i)