class car:
    def start(self):
        print("Car started")

class electric_car(car):
    def charge(self):
        print("charging bettery")

alto = electric_car()
alto.start()
alto.charge()
