import string
import random


class BureaucraticInformation:
    """generate all unique information for each car"""
    def generate_id(length):
        """generate the id for this vehicle"""
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_license_plate(id):
        """Generate the license plate"""
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class PayableTax():
    def __init__(self):
        self.tax = {}
        self.add_type_tax("Normal", 0.05)
        self.add_type_tax("Eletric", 0.02)

    def add_type_tax(self, type, tax):
        """Add the vehicles to the dictionary of vehicles"""
        self.tax[type] = [type, tax]

    def compute_tax(self, typeVehicle, price):
        """Compute the tax considering the price and the type of car"""
        return price*self.tax[typeVehicle][1]


class RegistryVehicle():
    """keep de register vehicles"""

    def __init__(self):
        self.vehicles = {}
        self.add_vehicles_to_registry("Tesla Model 3", "Eletric", 60000)
        self.add_vehicles_to_registry("Volkswagen ID3", "Eletric", 35000)
        self.add_vehicles_to_registry("BMW 5", "Normal", 45000)
        self.add_vehicles_to_registry("Tesla Model Y", "Eletric", 75000)

    def add_vehicles_to_registry(self, brand, typeVehicle, price):
        """Add the vehicles to the dictionary of vehicles"""
        tax = PayableTax()
        self.vehicles[brand] = [brand, typeVehicle,
                                price, tax.compute_tax(typeVehicle, price)]

    def print(self, brand):
        """print all the information required"""
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        id = BureaucraticInformation.generate_id(12)
        print(f"Id: {id}")
        print(
            f"License plate: {BureaucraticInformation.generate_license_plate(id)}")
        print(
            f"Payable tax: {self.vehicles[brand][3]}")


class Application:
    def create_registry(self, brand):
        vehicle = RegistryVehicle()
        vehicle.print(brand)


after = Application()
after.create_registry("Tesla Model Y")
