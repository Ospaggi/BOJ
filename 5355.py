#@는 3만큼 곱하기 
#%는 5만큼 더하기
##는 7만큼 빼기
#출력은 소슛점 2자리까지만
t=int(input())
for i in range (0,t):
	buf=input()
	n=int(buf[0])
	for j in buf:
		if isinstance(j,int) or isinstance(j,float): continue
		if j=='@': n*=3
		if j=='%': n+=5
		if j=='#': n-=7
	print("{:.2f}".format(n))
	
