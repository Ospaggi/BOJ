# <300
s=input()
score=40 if s[0]=='A' else 30 if s[0]=='B' else 20 if s[0]=='C' else 10
if s=="F": print("0.0")
elif s=="D-": print("0.7")
else: 
	score+=3 if s[1]=='+' else -3 if s[1]=='-' else 0
	print(str(score)[0],".",str(score)[1],sep='')
