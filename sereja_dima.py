a=int(input().strip())
b=list(map(int,input().strip().split()))
l=0
r=a-1
k=0
se=0
di=0
while(l<=r):
    c=max(b[l],b[r])
    if c==b[l]:
        l+=1
    else:
        r-=1
    if k%2==0:
        se+=c
    else:
        di+=c
    k+=1
print(se,di)
    