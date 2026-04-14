a=input().strip()
for i in a:
    if i!='4' and i!='7':
        a=int(a)
        if a%4==0 or a%7==0:
            print("YES")
        else:
            print("NO")
        break
else:
   print("YES")