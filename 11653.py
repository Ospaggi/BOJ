def prime(n):
	if (n==1): return;
	i=2
	while(n!=1):
		if (n%i==0):
			print(i)
			n=n//i
		else:
			i+=1
n=int(input())
prime(n)
