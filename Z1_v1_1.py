s = 0
for i in range(1, 13):
    s += i
print (s * 13)

g = 0
for i in range(13, 169):
    if i%13==0:
        g += i
print (g)
