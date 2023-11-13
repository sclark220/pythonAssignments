class Vehicle:
     def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

newAutomobile = Automobile((input("Enter Vehicle Type (Ex: Car, Truck, Boat): ")), (input("Enter Year: ")), (input("Enter Make: ")), (input("Enter Model: ")), (input("Enter number of doors: ")), (input("Is it a solid roof or sunroof: ")))

print(f"Vehicle type: {newAutomobile.vehicle_type}\n \
Year: {newAutomobile.year}\n \
Make: {newAutomobile.make}\n \
Model: {newAutomobile.model}\n \
Number of Doors: {newAutomobile.doors}\n \
Roof Type: {newAutomobile.roof}")   