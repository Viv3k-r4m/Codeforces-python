b=input().strip()
a=input().strip()
an=0
da=0
for i in a:
    if i=='A':
        an+=1
    elif i=='D':
        da+=1
if an>da:
    print("Anton")
elif an<da:
    print("Danik")
else:
    print("Friendship")