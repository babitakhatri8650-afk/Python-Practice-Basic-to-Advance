n=int(input("Enter number:"))
'''
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
'''
table=[n*i for i in range(1,11)]
print(table)