#Odd and even.
s=input()
start,end=0,len(s)-1
c=0
while(start<=end):
	if s[start]==s[end]: c+=1
	start+=1
	end-=1
print(c)
print(1 if c==len(s) else 0)
