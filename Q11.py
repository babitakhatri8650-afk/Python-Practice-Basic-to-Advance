with open ("old.txt") as f:
    content=f.read()
with open ("renamed_by_python","w") as f:
    f.write(content)