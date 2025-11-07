a=int(input().strip())
l=[]
for i in range(a):
    b,c=map(int,input().split())
    if c%2==0:
        l.append(0)
    else:
        l.append(b)

for i in l:
    print(i)