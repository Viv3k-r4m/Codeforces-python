a=int(input().strip())
b=0
for i in range(a):
    c=input().strip()
    if '+' in c:
        b+=1
    elif '-' in c:
        b-=1
print(b)