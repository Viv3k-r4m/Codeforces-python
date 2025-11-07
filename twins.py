a=int(input().strip())
b=list(map(int,input().strip().split()))
c=sum(b)
b.sort(reverse=True)
co=0
l=0
s1=0
while(l<a):
    c-=b[l]
    s1+=b[l]
    co+=1
    l+=1
    if c<s1:
        break
print(co)