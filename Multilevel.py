class person:
    def eat(self):
        print("person is eating")
class emp(person):
    def work(self):
        print("employee is working")
class teamleader(emp):
    def lead_team(self):
        print("Team Leader is leading the team")

p = teamleader()
p.eat()
p.work()
p.lead_team()