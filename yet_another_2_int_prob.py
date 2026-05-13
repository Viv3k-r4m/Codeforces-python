t=int(input().strip())
res=[]

for i in range(t):
    l,m=map(int,input().strip().split())
    s=abs(l-m)
    t=s//10
    u=s%10
    res.append(t+1 if u>0 else t)

for i in res:
    print(i)
