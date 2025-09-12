def change(a):
    if(len(a)>10):
        b=len(a[1:-1])
        d.append(a[0]+str(b)+a[-1])
    else:
        d.append(a)
c=int(input().strip())
d=[]
for i in range(c):
    b=input().strip()
    change(b)
for i in d:
    print(i)