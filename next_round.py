a,b=map(int,input().strip().split())
c=list(map(int,input().strip().split()))
d=c[b-1]
e=0
for i in range(len(c)):
    if c[i]>=d and c[i]>0:
        e+=1
    else:
        break
print(e)