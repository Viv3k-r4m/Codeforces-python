a=int(input().strip())
s=0
l=[100,20,10,5,1]
i=0
for i in l:
    s+=a//i
    a%=i
print(s)
