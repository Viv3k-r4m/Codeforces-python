n=int(input().strip())
b=list(map(int,input().strip().split()))
l=[]
for i in range(1,n+1):
    l.append((b[i-1],i))
l.sort()
for i in l:
    print(i[1],end=" ")
