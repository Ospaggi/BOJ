t=int(input())
for i in range(0,t):
    n=int(input())
    natural=input().split()
    sum=0
    for j in range(0,n):
        natural[j]=int(natural[j])
        sum+=natural[j]
    print(sum)