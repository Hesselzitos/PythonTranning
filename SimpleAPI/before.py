import string
import random


class GeneratorVehicleInfo:
    """generate all necessary vehicle information"""

    def generator_id(self, length):
        """generate the id for this vehicle"""
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_license_plate(self, id):
        """Generate the license plate"""
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def compute_tax(self, price, is_eletric):
        """Compute the tax considering the price and if is eletric"""
        if is_eletric:
            return price*0.02
        return price*0.05


class Vehicle:
    """Definition of vehicle"""

    def __init__(self, name, is_eletric, price):
        self.brand = name
        self.id = GeneratorVehicleInfo.generator_id(self, 12)
        self.license_plate = GeneratorVehicleInfo.generate_license_plate(
            self, self.id)
        self.eletric = is_eletric
        self.catalog_price = price

    def print(self):
        """print the necessary information"""
        print("Registration complete. Vehicle information:")
        print(f"Brand: {self.brand}")
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        print(
            f"Payable tax: {GeneratorVehicleInfo.compute_tax(self, self.catalog_price,self.eletric)}")


class Application:
    """Start the app"""

    def register_vehicle(self, brand, is_eletric, price):
        """Genarete the object vehicle"""
        vehicle = Vehicle(brand, is_eletric, price)
        vehicle.print()


before = Application()
before.register_vehicle("Volkswagen ID3", True, 7000)
