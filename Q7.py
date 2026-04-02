class vector:
    def __inti__(self,l):
        self.l=l

    def __add__(self,other):
        result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    
    def __mul__(self,other):
        result=vector(self.x*other.x,self.y*other.y,self.z*other.z)
        return result


    def __str__(self):
        return f"vector({self.x}x,{self.y}y,{self.z}z)"

    
    def __len__(self):
        return 3
v1=vector([2,4,5])
print(len(V1))