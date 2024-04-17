#Filthy code
#+: 0 0: 1 -: 2
#A: 1 B: 4 C: 7 D: 10
def main(s):
	n=0
	n+=1 if s[0]=="A" else 4 if s[0]=="B" else 7 if s[0]=="C" else 10
	n+=0 if s[1]=="+" else 1 if s[1]=="0" else 2
	grade=46
	for i in range(0,n): 
		grade-=3
		if str(grade)[1]=="4" and i>0: grade-=1
	rtrn=str(grade)[0]+"."+str(grade)[1]
	return rtrn
s=input()
print("0.0" if s=="F" else "0.7" if s=="D-" else main(s))
