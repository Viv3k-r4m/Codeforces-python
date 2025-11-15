import math
n = int(input())
groups = list(map(int, input().split()))

c1 = groups.count(1)
c2 = groups.count(2)
c3 = groups.count(3)
c4 = groups.count(4)

taxis = 0

# 1) groups of 4
taxis += c4

# 2) groups of 3 + 1
taxis += c3
c1 = max(0, c1 - c3)

# 3) groups of 2
taxis += c2 // 2
if c2 % 2:   # one group of 2 left
    taxis += 1
    c1 = max(0, c1 - 2)

# 4) remaining ones
taxis += math.ceil(c1/4)

print(taxis)
