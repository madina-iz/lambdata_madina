class Car:
    """ Car class to create Car objects """

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        self.color = color



    def drive(self):
        print("Driving")


    def set_mileage(self, new_mileage):
        self.mileage = new_mileage


    def fill_gas(self):
        print('Filling up on gas')


class ElectricCar(Car):

    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
        self.battery = Battery()

    def fill_gas(self):
        print("I don't have a gas tank")

    def set_mileage(self, new_mileage):
        super().set_mileage(new_mileage)


class Battery:

    def __init__(self, battery_size=100):
        self.battery_size = battery_size


def inc(x):
    """This is a function that takes a number and increments it by 1 """
    return x + 1