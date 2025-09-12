a=input().strip()
b="aeiouy"
c=""
for i in a:
    k=i.lower()
    if k not in b:
        c+="."+k
print(c)