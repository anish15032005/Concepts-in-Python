#we have three types of array sequences here
#LIST[],TUPLE(,) and STRING(""). All support Indexing
#8bits = 1 byte
#SAMPLE has 6 chars = 12 bytes
import sys
n = 10
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    
    data.append(n)