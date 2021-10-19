# a=int(input('a='))
# b=int(input('b='))
# while a<=b:
#     print(a)
#     a+=1
from sys import stdout
import numpy as np

i=1
while i<=9:
    a = np.full((i),i)
    print(*list(a), sep='')
    i+=1
