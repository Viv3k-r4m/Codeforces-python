n=int(input().strip())
p=[]
for i in range(n):
    p.append(input().strip())
c=1
for i in range(n-1):
    if p[i]!=p[i+1]:
        c+=1
print(c)