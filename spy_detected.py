from collections import Counter
t=int(input().strip())
res=[]

for i in range(t):
    n=int(input().strip())
    l=list(map(int,input().strip().split()))
    r=Counter(l)
    for i in range(n):
        if r[l[i]]==1:
            res.append(i+1)
            break

for i in res:
    print(i)
