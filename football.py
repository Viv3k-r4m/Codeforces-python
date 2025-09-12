a=input().strip()
for i in range(len(a)-6):
    if(a[i:i+7].count('0')==7 or a[i:i+7].count('1')==7):
        print("YES")
        break
else:
    print("NO")