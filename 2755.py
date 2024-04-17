#2754 Recycle (might look awful)
t=int(input())
g=[]
for i in range(0,t):
	buf,cr,s=input().split()
	score=40 if s[0]=='A' else 30 if s[0]=='B' else 20 if s[0]=='C' else 10
	if s=="F": g.append("0.0")
	elif s=="D-": print("0.7")
	else: 
		score+=3 if s[1]=='+' else -3 if s[1]=='-' else 0
		g.append(str(score)[0]+"."+str(score)[1])
	g[i]=float(g[i])
print(round(t/sum(g),2))
