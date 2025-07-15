from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, max_cargo):
        super().__init__()
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        total_cargo = self.cargo + cargo
        if total_cargo > self.max_cargo:
            raise CargoOverload

        self.cargo = total_cargo

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo