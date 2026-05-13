t=int(input().strip())
res=[]

for i in range(t):
    l,m,n=map(int,input().strip().split())
    s=(l+m+n)-max(l,m,n)-min(l,m,n)
    res.append(s)

for i in res:
    print(i)
