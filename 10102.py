v=int(input())
a,b=0,0
s=input()
for i in s:
	if i=='A': a+=1
	else: b+=1
print("A" if a>b else "B" if a<b else "Tie")
