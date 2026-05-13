t=int(input().strip())
res=[]

for i in range(t):
    l=input().strip().split()
    res.append(l[0][0]+l[1][0]+l[2][0])

for i in res:
    print(i)