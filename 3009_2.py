#if으로만
x1,y1=input().split()
x2,y2=input().split()
x3,y3=input().split()
x1,x2,x3,y1,y2,y3=int(x1),int(x2),int(x3),int(y1),int(y2),int(y3)
if x1==x2: print(x3,end=' ')
elif x1==x3: print(x2,end=' ')
else: print(x1,end=' ')
if y1==y2: print(y3)
elif y1==y3: print(y2)
else: print(y1)
