def divisible5(n):
    if n%5==0:
        return True
    return False

a=[4,35,48735,234,22,77,8875]
f=list(filter(divisible5,a))

print(f)