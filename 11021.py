#A와  B는  1~9 사 이 의  정 수
n=int(input())
for i in range(0,n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print(f"Case #{i+1}: {a+b}")
