#Filthy code
#아 다 적고나니 현타 씨게오네
pointX=[]
pointY=[]
for i in range(0,3):
	a,b=input().split()
	pointX.append(int(a))
	pointY.append(int(b))
p=pointX[0]
q=pointY[0]
#xCount와 yCount는 각각 첫 입력을 기준으로 하고 있음
xCount,yCount=0,0
xDiff,yDiff=0,0
for i in range(0,3):
	xCount+=1 if p==pointX[i] else 0
	yCount+=1 if q==pointY[i] else 0
	xDiff=pointX[i] if p!=pointX[i] else xDiff
	yDiff=pointY[i] if q!=pointY[i] else yDiff
#Count가 2가 된다는 것은 첫 입력과 같은 숫자가 하나 더 있다는것 -> Diff를 출력
#1이면 자기 혼자라는것 -> p 또는 q를 출력
print(f"{xDiff} " if xCount==2 else f"{p} ",end='')
print(yDiff if yCount==2 else q)
