class student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = None
        self.set_grade(grade)
        
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade.")

    def get_grade(self):
        return self.__grade
s1 = student("Jay", 85)
print(s1.name) 
print(s1.get_grade()) 

s1.set_grade(105)
print(s1.get_grade())