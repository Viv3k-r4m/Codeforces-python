a=int(input().strip())
b=""
if a==1:
    print("I hate it")
else:
    for i in range(a):
        if i%2==0:
            b+="I hate"
        else:
            b+="I love"
        if i!=(a-1):
            b+=" that "
    b+=" it"
    print(b)
