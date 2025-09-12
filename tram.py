a=int(input().strip())
mx=0
s=0
for i in range(a):
    b,c=map(int,input().strip().split())
    s-=b
    #mx=max(mx,s)
    s+=c
    mx=max(mx,s)
print(mx)