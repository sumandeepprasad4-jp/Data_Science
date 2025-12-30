class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        return self.length * self.breath
    def __add__(self,other):
        return self.length + other.length
r1=Rectangle(2,6)
r2=Rectangle(4,5)
print(r1.area())
print(r2.area())
print(r1+r2)