from base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine

