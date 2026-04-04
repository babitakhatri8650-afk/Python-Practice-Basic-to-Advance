try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    print(a/b)
except ZerodivisionError as v:
    print("Infinite")