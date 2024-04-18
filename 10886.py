n=int(input())
cute=0
notcute=0
for i in range(0,n): 
	if input()=='1': cute+=1
	else: notcute+=1
print("Junhee is"+(" not " if cute<notcute else " ")+"cute!")

