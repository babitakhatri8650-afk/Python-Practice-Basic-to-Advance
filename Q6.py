with open ("log.txt") as f:
    content=f.read()
if "python" in content :
    print("Yes python is present in content")
else:
    print("Python is not present in content")

