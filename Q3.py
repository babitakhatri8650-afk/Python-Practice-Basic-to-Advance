class demo:
    a=4
object=demo()
print(object.a) #prints the class attribute because instance attribute is not present
object.a=0 #instance attribute is set
print(object.a)# prints the instance attribute because instance attribute is present
print(demo.a)   #class attribute not change