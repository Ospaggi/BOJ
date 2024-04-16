def dice(n,max):
	if n[0]==n[1] and n[1]==n[2]: return 10000+n[1]*1000
	if n[0]==n[1] or n[1]==n[2]: return 1000+n[1]*100
	if n[0]==n[2]: return 1000+n[0]*100
	return max*100
n=int(input())
prize=[]
max_p=0
for i in range(0,n): 
	p=input().split()
	max=0
	for j in range(0,3): 
		p[j]=int(p[j])
		if max<p[j]: max=p[j]
	prize.append(dice(p,max))
	if prize[i]>max_p: max_p=prize[i]
print(max_p)
