a=int(input().strip())
l=[]
for i in range(a):
    b=int(input().strip())
    c=list(map(int,input().split()))
    l.append(max(c))
for i in l:
    print(i)