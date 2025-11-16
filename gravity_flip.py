a=int(input().strip())
b=list(map(int,input().strip().split()))
b.sort()
print(*b)