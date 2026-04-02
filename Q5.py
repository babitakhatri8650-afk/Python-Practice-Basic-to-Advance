class vector:
    def __inti__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    
    def __mul__(self,other):
        result=vector(self.x*other.x,self.y*other.y,self.z*other.z)
        return result


    def __str__(self):
        return f"vector({self.x}x,{self.y}y,{self.z}z)"
v1=vector(2,4,5)
v2=vector(3,5,6)
v3=vector(4,6,7)

print(v1+v2)
print(v1*v2)
        
  
        