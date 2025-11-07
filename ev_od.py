import math
a,b=map(int,input().strip().split())
ce=math.ceil(a/2)
xce=ce+1
nfact=-(ce-1)
if b>ce:
    print(2*b+nfact-xce)
else:
    print(2*b-1)