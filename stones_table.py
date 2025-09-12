a=int(input().strip())
b=input().strip()
c=0
d=0
for i in range(len(b)-1):
    if b[i]==b[i+1]:
        c+=1
    else:
        d+=c
        c=0
d+=c
print(d)