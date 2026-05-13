l=list(map(int,input().strip().split()))
l.sort()
c=l[-1]-l[0]
b=l[-1]-l[1]
a=l[-1]-c-b

print(a,b,c)