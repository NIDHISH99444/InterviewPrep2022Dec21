# @SOLID principles  ->   D - dependency inversion


from abc import  ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light turn on")

    def turn_off(self):
        print("Light turn off")


class Fan(Switchable):
    def turn_on(self):
        print("Fan turn on")

    def turn_off(self):
        print("Fan turn off")


class ElectricPowerSwitch:
    #
    # def __init__(self, l: LightBulb):    # had dependency on light bulb
    #     self.lightbulb = l
    #     self.on = False

    def __init__(self, s: Switchable):
        self.client = s
        self.on = False

    def press(self):
        if self.on:
            self.on=False
            self.client.turn_off()
        else:
            self.on = True
            self.client.turn_on()

# s=Switchable()
light=LightBulb()
fan=Fan()
# e=ElectricPowerSwitch(light)
e=ElectricPowerSwitch(fan)
e.press()
e.press()