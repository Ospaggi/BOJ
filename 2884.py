h,m=map(int, input().split())
s=3600*h+60*(m-45)
if s<0: s=86400+s
print(f"{s//3600} {(s-(s//3600)*3600)//60}")
