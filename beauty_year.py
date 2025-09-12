a=int(input().strip())
a+=1
while(True):
    c=set(str(a))
    if(len(c)==4):
        print(a)
        break
    a+=1

