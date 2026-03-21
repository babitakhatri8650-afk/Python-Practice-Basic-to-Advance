class calculator:
    def __init__(self,n):
        self.n=n

    def sqaure(self):
        print(f"The sqaure of the number is {self.n*self.n}")
    def cube(self):
        print(f"The cube of the number is {self.n*self.n*self.n}")
    def sqaureroot(self):
        print(f"The sqaureroot of the number is {self.n**1/2}")
a=calculator(4)
a.sqaure()
a.sqaureroot()
a.cube()
       
        