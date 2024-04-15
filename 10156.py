#한 개 가격=K 사려고 하는 과자의 개수=N 현재 잔액=M
k,n,m=input().split()
k,n,m=int(k),int(n),int(m)
print(k*n-m if k*n-m>0 else 0)
