def my_decorator(func):
    def wrapper():
        print("Befor functions run")
        func()
        print("After Function Run")
    return wrapper
@my_decorator
def greet():
    print("Hello")
    
greet()