with open ("file1.txt" )as f:
    content1=f.read()

with open ("file2.txt") as f:
    content2=f.read()

if (content1==content2):
    print("Yes both content are same")
else:
    print("No both content are not same")