"""
Доработайте класс `Vehicle`
"""

from abc import ABC

from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight = 2000, fuel = 70, fuel_consumption = 8):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            return

        if self.fuel <= 0:
            raise LowFuelError

        self.started = True

    def move(self, distance):
        fuel_required = (distance/100) * self.fuel_consumption
        if fuel_required > self.fuel:
            raise NotEnoughFuel

        self.fuel -= fuel_required


