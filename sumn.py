a=int(input().strip())
l=[]
for i in range(a):
    b=list(map(int,input().strip().split()))
    c=max(b)
    d=min(b)
    e=sum(b)-(c+d)
    if d+e==c:
        l.append("YES")
    else:
        l.append("NO")
for i in l:
    print(i)