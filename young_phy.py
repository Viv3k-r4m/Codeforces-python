a=int(input().strip())
b=[list(map(int,input().strip().split())) for _ in range(a)]
x,y,z=0,0,0
for i in range(len(b)):
    x+=b[i][0]
    y+=b[i][1]
    z+=b[i][2]
if(x==0 and y==0 and z==0):
    print("YES")
else:
    print("NO")