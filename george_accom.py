a=int(input().strip())
d=0
for i in range(a):
    b,c=map(int,input().strip().split())
    if c-b>=2:
        d+=1
print(d)
