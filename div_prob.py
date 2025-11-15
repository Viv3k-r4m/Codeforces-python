a=int(input().strip())
b=[]
for i in range(a):
    c,d=map(int,input().strip().split())
    if c<d:
        b.append(d-c)
    else:
        e=c//d
        f=c%d
        if f!=0:
            b.append(((e+1)*d)-c)
        else:
            b.append(0)
for i in b:
    print(i)
