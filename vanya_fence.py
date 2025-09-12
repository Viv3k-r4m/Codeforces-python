a,b=map(int,input().split())
c=list(map(int,input().split()))
w=0
for i in c:
    if i>b:
        w+=2
    else:
        w+=1
print(w)