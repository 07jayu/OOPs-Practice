def counter():
    count = 0
    def visit():
        nonlocal count
        count += 1
        return count
    return visit

visit = counter()
print(visit())  
print(visit())  
print(visit())  
print(visit())  