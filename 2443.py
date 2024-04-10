#2n-1
n=int(input())
star=2*n-1
for i in range(0,n):
    for j in range(0,i): print(" ",end='')
    for k in range(0,star): print("*",end='')
    star-=2
    print()