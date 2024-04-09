a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(input())
totsec=3600*a+60*b+c+d
if totsec >= 86400: 
    totsec-=86400*(totsec//86400)
min=(totsec-(totsec//3600)*3600)//60 
print(f"{totsec//3600} {min} {totsec-(totsec//3600)*3600-min*60}")