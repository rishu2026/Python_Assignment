class Vehicle():
    def __init__(self,vehicle_id,brand):
        self.vehicle_id=vehicle_id
        self.brand=brand

    def calculate_rent(self):
        raise NotImplementedError("Subclass must implement calculate_rent()")


class Car(Vehicle):
    def __init__(self,vehicle_id,brand,price_per_day,no_of_day):
        super().__init__(vehicle_id,brand)
        self.price_per_day=price_per_day
        self.no_of_day=no_of_day

    def calculate_rent(self):
        print("Car Rent will be" ,self.price_per_day*self.no_of_day)

class Bike(Vehicle):
    def __init__(self,vehicle_id,brand,price_per_hour,no_of_hour):
        super().__init__(vehicle_id,brand)
        self.price_per_hour=price_per_hour
        self.no_of_hour=no_of_hour

    def calculate_rent(self):
        print("Bike Rent will be" ,self.price_per_hour*self.no_of_hour)

class Truck(Vehicle):
    def __init__(self,vehicle_id,brand,price_per_km,no_of_km):
        super().__init__(vehicle_id,brand)
        self.price_per_km=price_per_km
        self.no_of_km=no_of_km

    def calculate_rent(self):
        print("Truck Rent will be" ,self.price_per_km*self.no_of_km)

vehicles = [
    Car(1234,"Alto",500,4),
    Bike(1232,"Apache",100,3),
    Truck(1234,"Ashok Leyland",78,246)
]

for v in vehicles:
    v.calculate_rent()