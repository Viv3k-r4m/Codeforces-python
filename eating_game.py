a=int(input().strip())
res=[]
for i in range(a):
    n=int(input().strip())
    a=list(map(int,input().strip().split()))
    c=0
    k=max(a)
    for i in a:
        if i==k:
            c+=1
    res.append(c)

for i in res:
    print(i)