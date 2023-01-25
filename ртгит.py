class Racer:
    def drive(self):
        print ("Drive very fast")

class Car:
    def drive (self):
        print ("Drive")

class RacingCar(Car,Racer):
    pass


car = RacingCar()
car.drive()