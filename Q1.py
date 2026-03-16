f=open("poem.txt")
content=f.read()

if "twinkle" in content:
    print("Yes the word twinkle is present in the content")
else:
     print("Yes the word twinkle is not present in the content")

f.close()