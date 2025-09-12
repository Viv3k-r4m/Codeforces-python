a=input().strip()
b=set()
for i in a:
    b.add(i)
if(len(b)%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")