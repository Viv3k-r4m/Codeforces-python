a=input().strip()
b="hello"
l=0
r=0
c=len(a)
d=len(b)
while(l<c and r<d):
    if a[l]==b[r]:
        r+=1
    l+=1
print("YES") if r==d else print("NO")
