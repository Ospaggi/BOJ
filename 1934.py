#Filthy code
def least(a,b):
	i=2
	lcd=1
	while(a!=1 or b!=1):
		j=False
		if (a%i==0):
			a=a/i
			lcd*=i 
			j=True
		if (b%i==0):
			b=b/i
			lcd*=1 if j else i
		i+=1
	return lcd
t=int(input())
for i in range(0,t):
	a,b=input().split()
	a=int(a)
	b=int(b)
	print(least(a,b))
