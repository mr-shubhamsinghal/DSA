
from abc import ABC, abstractmethod



class Events(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass


class Sensor(Events):

    def on(self):
        print("Sensor on")
    
    def off(self):
        print("Sensor off")

class Lights(Events):

    def on(self):
        print("Lights on")
    
    def off(self):
        print("Lights off")

class Smoke(Events):

    def on(self):
        print("Smoke on")
    
    def off(self):
        print("Smoke off")

class Singleton(type):
    
    __instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class Facade(metaclass=Singleton):
    def __init__(self):
        self.__sensor = Sensor()
        self.__lights = Lights()
        self.__smoke = Smoke()
    
    def Emergency(self):
        self.__sensor.on()
        self.__lights.on()
        self.__smoke.on()
    
    def NoEmergency(self):
        self.__sensor.off()
        self.__lights.off()
        self.__smoke.off()



if __name__ == "__main__":
    facade = Facade()
    facade.Emergency()
    facade.NoEmergency()
