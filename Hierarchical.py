class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def write_code(self):
        print("Developer writing code")

class Designer(Employee):
    def design_ui(self):
        print("Designer designing UI")

class Tester(Employee):
    def test_app(self):
        print("Tester testing app")

d = Developer()
de = Designer()
t = Tester()

d.work(); d.write_code()
de.work(); de.design_ui()
t.work(); t.test_app()
