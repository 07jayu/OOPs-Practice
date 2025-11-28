def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__}called")
        return func(*args, **kwargs)
    return wrapper

@logger

def add(a,b):
    return a+b
print(add(5,10))