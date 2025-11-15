a=int(input().strip())
b={}
d=[]
for i in range(a):
    c=input().strip()
    b[c]=b.get(c,0)+1
    if b[c]>1:
        d.append(c+str(b[c]-1))
    else:
        d.append("OK")
for i in d:
    print(i)
