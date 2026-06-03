#Q1 break when i==7

for i in range(1,11):
    #print(i)
    if(i==7):
        break
    print(i)

#Q2 skipping the number 5

for n in range(1,11):
    if(n==5):
        continue
    print(n)

#Q3
for p in range(1,6):
    match p:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            pass
        case 4:
            print(4)
        case 5:
            print(5)
