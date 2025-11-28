def outer():
    x = 10
    def inner():
        print(x)
    return inner
f = outer()
f()  

def discount_creator(discount):
    def apply(price):
        return price - (price * discount / 100)
    return apply

discount10 = discount_creator(10)
discount20 = discount_creator(20)
print(discount10(100))  # Output: 90
print(discount20(100))  # Output: 80