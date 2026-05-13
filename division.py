t=int(input().strip())
res=[]

for i in range(t):
    l=int(input().strip())
    if l>=1900:
        s="Division 1"
    elif 1600<=l<1900:
        s="Division 2"
    elif 1400<=l<1600:
        s="Division 3"
    else:
        s="Division 4"
    res.append(s)

for i in res:
    print(i)
