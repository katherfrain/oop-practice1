class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def print_info(car):
        print(car.year, car.make, car.model)

tesla = Vehicle("Tesla", "CyberTruck", "2019")
Vehicle.print_info(tesla)