class Teacher:
    def teach(self):
        print("Teaching students")

class MathTeacher(Teacher):
    def teach_math(self):
        print("Teaching Mathematics")

class ScienceTeacher(Teacher):
    def teach_science(self):
        print("Teaching Science")

class HeadOfDepartment(MathTeacher, ScienceTeacher):
    pass

hod = HeadOfDepartment()
hod.teach()
hod.teach_math()
hod.teach_science()
