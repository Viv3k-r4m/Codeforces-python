a=int(input().strip())
b=list(map(int,input().strip().split()))
s=0
for i in range(a):
    s+=b[i]/100
print((s/a)*100)