# method overloading whic is not spporte by python because it overright the method
class A:
    def add(self, num1, num2):
        return num1 + num2

    def add(self, num1, num2, num3):
        return num1 + num2 + num3


obj = A()
print(obj.add(1, 2, 3))


# method overriding
class A:
    def add(self, num1, num2):
        return num1 + num2


class B:
    def add(self, num1, num2, num3):
        return num1 + num2 + num3


obj = A()
obj2 = B()
print(obj2.add(5, 1, 2))
print(obj.add(5, 8))
