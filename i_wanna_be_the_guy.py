n=int(input().strip())

s=set(list(map(int,input().strip().split()))[1:])

t=set(list(map(int,input().strip().split()))[1:])

p=s|t

if 0 in p:
    p.remove(0)
if p=={i for i in range(1,n+1)}:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")