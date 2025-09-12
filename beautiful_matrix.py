c=[]
for i in range(5):
    c.append(list(map(int,input().strip().split())))
for i in range(5):
    for j in range(5):
        if(c[i][j]==1):
            a=i
            b=j
            break
print(abs(2-a)+abs(2-b))