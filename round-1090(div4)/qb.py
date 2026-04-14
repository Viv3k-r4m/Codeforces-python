t=int(input().strip())
res=[]
for i in range(t):
    l=list(map(int,input().strip().split()))
    n=len(l)
    l.sort()
    s=0
    for j in range(n-1):
        s+=(-l[j])
    s+=l[n-1]
    res.append(s)

for i in res:
    print(i)
