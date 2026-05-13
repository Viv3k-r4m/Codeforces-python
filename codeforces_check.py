t=int(input().strip())
res=[]

for i in range(t):
    r=input().strip()
    res.append("YES" if r in "codeforces" else "NO")

for i in res:
    print(i)