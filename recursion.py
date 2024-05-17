#Display the sum of n numbers.

def recur(n):
    if n==1:
        return 1
    else:
        return n+recur(n-1)

    

print(recur(10))

#Calculate the factorial of a number.

def factori(s):
    if s==1:
        return 1
    else:
        return s*factori(s-1)
    

print(factori(999))
