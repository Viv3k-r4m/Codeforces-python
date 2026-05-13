l=input().strip()

n=len(l)
s=""

i=0

while i<n:
    if l[i]=='-':
        if l[i+1]=='.':
            s+="1"
        else:
            s+="2"
        i+=2
    else:
        s+="0"
        i+=1
print(s)