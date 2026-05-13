t=int(input().strip())
res=[]

for i in range(t):
    n=int(input().strip())
    l=list(map(int,input().strip().split()))
    s=sum(l)
    if s%2==0:
        res.append("YES")
    else:
        res.append("NO")

for i in res:
    print(i)
