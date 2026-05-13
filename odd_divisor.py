t=int(input().strip())
res=[]

for i in range(t):
    l=int(input().strip())
    res.append("YES" if l&(l-1)!=0 else "NO")

for i in res:
    print(i)

"""Quick Methods to Check
Division Method: Continuously divide the number by 2 as long as it's even. 
If you end up with a result greater than 1, that result is an odd divisor.

Bitwise Shortcut (Programming): 
A number n has an odd divisor (>1) if the following bitwise check is true:

n & (n - 1) != 0
If this result is non-zero, it means n is not a power of 2 and therefore does have an odd divisor.
"""
