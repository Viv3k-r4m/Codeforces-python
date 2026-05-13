t=int(input().strip())
res=[]

for i in range(t):
    l,m,n=map(int,input().strip().split())
    res.append('+' if l+m==n else '-')

for i in res:
    print(i)
