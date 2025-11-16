a,b=map(int,input().strip().split())
c=[]
for i in range(b):
    c.append(tuple(map(int,input().strip().split())))
c.sort()
for i,j in c:
    if a>i:
        a+=j
    else:
        print("NO")
        break
else:
    print("YES")
