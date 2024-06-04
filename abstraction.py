# Import required modules
from abc import ABC, abstractmethod

# Create Abstract base class
class DefenceForce(ABC):
    def __init__(self):
        self._gun = "AK47"

    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print(f"Gun = {self._gun}")

class Force(DefenceForce):
    pass

class Army(Force):
    def area(self):
        print("Army Area = Land")

class AirForce(DefenceForce):
    def area(self):
        print('Airforce Area = Sky')

class Navy(DefenceForce):
    def area(self):
        print('Navy Area = Sea')

army = Army()
army.gun()
army.area()

airforce = AirForce()
airforce.gun()
airforce.area()

navy = Navy()
navy.gun()
navy.area()