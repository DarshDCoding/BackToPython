# 7. Smart Home Automation Engine
# Key Concepts: Multiple Inheritance, Mixins, Property Decorators.
# Goal: Create standalone mixin classes like `WiFiConnectedMixin` and `BatteryPoweredMixin`. Combine these with base device classes (`Light`, `Thermostat`) to create hybrid devices (e.g., `SmartThermostat`).
# Use `@property` getters and setters with validation logic to restrict device settings (e.g., temperature limits).

#Mixin Classes as I understood
class WiFiConnectedMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._connected = False

    def connect(self) ->bool:
        self._connected = True
        print("Connected to WiFi")
        return True


class BatteryPoweredMixin:
    def __init__(self, **kwargs): #best practice to add an __init__ and super() for MRO
        super().__init__(**kwargs)
        self._battery_percentage = 0

    def add_battery(self, battery_percentage)->bool:
        self._battery_percentage += battery_percentage
        print("Battery Powered")
        return True

#Base Device
class BaseDevice:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

#Base Devices
class Light (BaseDevice):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)


class Thermostat(BaseDevice):
    _temperature = 27
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self._temperature = Thermostat._temperature

    @property
    def temperature(self):
        print(f"Current Temperature is: {self._temperature}°C ")
        return self._temperature


    @temperature.setter
    def temperature(self, temperature:int):
        if temperature > 52:
            print("Be Bhunn Jayega...")
            return
        elif temperature == self._temperature:
            print("Chutiye already itna hi hai.")
            return
        elif temperature <= 0:
            print("Murda Chupa rakha hai ghar me?")
            return
        self._temperature = temperature


#Hybrid devices
class SmartThermostat(Thermostat, WiFiConnectedMixin, BatteryPoweredMixin):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

class SmartLight(Light, WiFiConnectedMixin):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

smartThermoStat = SmartThermostat("Thermostat1")

smartThermoStat.add_battery(55)
smartThermoStat.connect()
print(smartThermoStat.temperature)
smartThermoStat.temperature = 10
print(smartThermoStat.temperature)
print(smartThermoStat.connect())
print(SmartThermostat.__mro__)