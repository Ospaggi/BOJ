a,b=input().split()
a=int(a)
b=int(b)
c=int(input())
totsec=3600*a+60*b+60*c
if totsec>=86400: totsec-=86400
print(f"{totsec//3600} {(totsec-(totsec//3600)*3600)//60}")
