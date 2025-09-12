a=int(input().strip())
c=0
for i in range(a):
    b=list(map(int,input().strip().split())).count(1)
    if(b>1):
        c+=1
print(c)