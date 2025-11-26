class Employee:
    def work(self):
        print("Employee is working")

class Trainer:
    def train(self):
        print("Trainer is teaching new skills")

class ProjectManager(Employee, Trainer):
    pass

pm = ProjectManager()
pm.work()
pm.train()
