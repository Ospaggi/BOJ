#r: expected revenue if no ads
#e: expected revenue if i run ads
#c: ad cost
n=int(input())
for i in range(0,n):
	r,e,c=map(int,input().split())
	if r<e-c: print("advertise")
	elif r==e-c: print("does not matter")
	else: print("do not advertise")
