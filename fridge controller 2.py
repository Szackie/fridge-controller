import time

class Observer:
    def update(self, subject):
        pass

class FridgeTemperatureObserver(Observer):
    def update(self, subject):
        if subject.fridge_temp != subject.programmed_temp:
            subject.adjust_temp()

class Fridge:
    def __init__(self, fridge_temp: float, outside_temp: float, programmed_temp: float):
        self.fridge_temp = fridge_temp
        self.outside_temp = outside_temp
        self.programmed_temp = programmed_temp
        self.observers = []
        self.fan_on = False
        self.vent_open = False
        self.out_in_diff=fridge_temp-outside_temp if fridge_temp>outside_temp else 0

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def adjust_temp(self):
        if self.fridge_temp > self.programmed_temp:
            if self.fridge_temp > self.outside_temp:
                #open air vent to cool down the fridge
                self.vent_open = True
                self.fan_on = False
            else:
                #turn on the fan to cool down the fridge
                self.fan_on = True
                self.vent_open = False
        else:
            #close air vent and turn off the fan
            self.vent_open = False
            self.fan_on = False

    def set_temperature(self, fridge_temp: float, outside_temp: float):
        self.fridge_temp = fridge_temp
        self.outside_temp = outside_temp
        self.out_in_diff=fridge_temp-outside_temp if fridge_temp>outside_temp else 0

        self.notify()

    def get_programmed_temp(self):
        return self.programmed_temp

    def get_fridge_temp(self):
        return self.fridge_temp
    
    def get_vent_status(self):
        return "OPEN" if self.vent_open else "CLOSED"
    
    def get_fan_status(self):
        return "ON" if self.fan_on else "OFF"

    def update_temperature(self):
        if self.fan_on:
            self.fridge_temp -= 0.1
        if self.vent_open:
            if self.fridge_temp > self.outside_temp:
                self.fridge_temp -= (self.out_in_diff) / 10
            else:
                self.vent_open = False
        self.notify()


#TESTS
        
def test_fridge():
    fridge = Fridge(20.0, 17.0, 15.0)
    observer = FridgeTemperatureObserver()
    fridge.attach(observer)

    # Test 1: Fridge temperature is higher than outside and programmed temperature
    while fridge.fridge_temp - fridge.programmed_temp > 0.1:
        print("Fridge temperature: ", fridge.get_fridge_temp())
        print("Vent status: ", fridge.get_vent_status())
        print("Fan status: ", fridge.get_fan_status())
        # time.sleep(1)
        fridge.update_temperature()
    assert fridge.fridge_temp - fridge.programmed_temp <= 0.1


    # Test 2: Fridge temperature is lower than outside but higher than programmed temperature
    fridge.set_temperature(16.0, 20.0)
    fridge.update_temperature()
    assert fridge.fridge_temp < 16.0

    # Test 3: Fridge temperature is lower than programmed temperature
    fridge.set_temperature(14.0, 20.0)
    fridge.update_temperature()
    assert fridge.fridge_temp == 14.0

test_fridge()