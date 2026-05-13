arr=[0]*26
n=int(input().strip())
l=input().strip()

for i in l:
    x=i.lower()
    arr[ord(x)-ord('a')]+=1

for i in range(26):
    if arr[i]==0:
        print("NO")
        break
else:
    print("YES")