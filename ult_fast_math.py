a="0b"+input().strip()
b="0b"+input().strip()
res=bin(int(a,2)^int(b,2))[2:]
res=res.rjust(len(a)-2,'0')
print(res)