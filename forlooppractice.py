#Display the pattern:
#|
#| |
#| | |
#| | | |
#| | | | |
def add(sim,n):
    for i in range(1,n+1):
        print(sim*i)
add("@",12)
add("#",15)
#Display reverse pattern:
#- - - - -
#- - - -
#- - -
#- -
#-
def sub(sin,g):
    for t in range(g,0,-1):
        print(sin*t)
sub("&",12)

"""Display all the numbers but replace every multiple of 3 by the word BINGO.
Output: 
1
2
BINGO
4
5
BINGO...."""
r=int(input("how long do you want it to be"))
for e in range(1,r+1):
    if e%3==0:
        print("bingo")

    else:
        print(e)