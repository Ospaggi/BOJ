#Filthy code
#2754 Recycle (might look horrendous)
# 0.0 -> 0
# 0.7 -> 7
# 1.0 -> 10
# 25.7 -> 257
t=int(input())
g=[]
totalcr=0
for i in range(0,t):
	buf,cr,s=input().split()
	score=40 if s[0]=='A' else 30 if s[0]=='B' else 20 if s[0]=='C' else 10
	if s=="F": g.append(0)
	elif s=="D-": g.append(7)
	else: 
		score+=3 if s[1]=='+' else -3 if s[1]=='-' else 0
		g.append(score)
	g[i]=int(g[i])*int(cr)
	totalcr+=int(cr)
res=str(sum(g)/totalcr/10) 
if res[len(res)-1]=="5": res=float(res)+5*10**(-len(res)-2)
else: res=round(float(res),2)
print("%.2f" % res)
