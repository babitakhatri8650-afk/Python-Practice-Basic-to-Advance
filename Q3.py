class employee:
    salary=234
    increment=20
    @property
    def Salaryafterincrement(self):
        return self.salary + self.salary*(self.increment/100)
    @Salaryafterincrement.setter
    def Salaryafterincrement(self,salary):
        
        self.increment=((salary/self.salary)-1)/100


e=employee()
print(e.Salaryafterincrement)
print(e.Salaryafterincrement)
print(e.increment)