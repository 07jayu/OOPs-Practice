# Make a class Calculator with methods: add, sub, mul, div.

class cal:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print(self.num1 + self.num2)
    def sub(self):
        print(self.num1 - self.num2)
    def div(self):
        print(self.num1 / self.num2)
    def mul(self):
        print(self.num1 * self.num2)

c1 = cal(10,5)
c1.add()
c1.sub()
c1.mul()
c1.div()
