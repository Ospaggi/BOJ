ans=[]
while(True):
	a,b=input().split()
	a,b=int(a),int(b)
	if a==0 and b==0: break
	else: ans.append(a>b)
for i in ans: print("Yes" if i else "No")
