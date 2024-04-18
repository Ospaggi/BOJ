#( = 10cm
#) = 10cm
#(( = 15cm
#((( = 20cm
#() = 20cm
#()) = 25cm
s=input()
h=10
for i in range(1,len(s)): h+=5 if s[i-1]==s[i] else 10
print(h)
