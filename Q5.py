from functools import reduce
l=[4,35,48735,234,22,77,8875]

def greater(a,b):
    if a>b:
        return a
    return b

print(reduce(greater,l))