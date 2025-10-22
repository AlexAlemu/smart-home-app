# Task 1
'''
Class describing a smart plug 
'''
class SmartPlug:
    def __init__(self, consumption_rate):
        self._switched_on = False
        if 0 <= consumption_rate <= 150:
            self._consumption_rate = consumption_rate
        else:
            raise ValueError (f"Invalid rate of {consumption_rate}. Initialisation blocked. Consumption rate must be between 0 and 150.")
        
       
    @property
    def consumption_rate(self):
        return self._consumption_rate
   
    @consumption_rate.setter
    def consumption_rate(self, value):
        if 0 <= value <= 150:
            self._consumption_rate = value
        else:
            raise ValueError (f"Unable to update to {value}. Consumption rate must be between 0 and 150.")
   
    def toggle_switch(self):
        self._switched_on = not self._switched_on
   
    def __str__(self):
        state = "on" if self._switched_on else "off"
        output = f"SmartPlug is {state} with a consumption rate of {self._consumption_rate}"
        return output
   

# Function that tests the SmartPlug class
def test_smart_plug():
    plug1 = SmartPlug(45)
    print(plug1)
    plug1.toggle_switch()
    print(plug1)
    plug1.consumption_rate = 75
    print("New consumption rate is", plug1.consumption_rate, "Watts")
    print(plug1)
    plug1.toggle_switch()
    print(plug1)
    
    # Second phase testing
    print("-------------------------------------------")
    print("Trying to update invalid consumption rates:")
    print("-------------------------------------------")
    try:
        plug1.consumption_rate = -10
    except ValueError as e:
        print(f"Error: {e}")
    
    print("Consumption rate remained", plug1.consumption_rate, "Watts")
    print(plug1)
    
    try:
        plug1.consumption_rate = 200
    except ValueError as e:
        print(f"Error: {e}")
    
    print("Consumption rate remained", plug1.consumption_rate, "Watts")
    print(plug1)
    
    print("--------------------------------------------------------------------------")
    print("Trying to create 2 more SmartPlug objects with invalid consumption rates:")
    print("--------------------------------------------------------------------------")
    try: 
        plug2 = SmartPlug(-5)
    except ValueError as e:
        print(f"Error: {e}")    

    try: 
        plug3 = SmartPlug(160)
    except ValueError as e:
        print(f"Error: {e}")  
  
  
# Task 2

'''
Parent/Base class
'''
class SmartDevice:
    def __init__(self):
        self._switched_on = False
        
    def toggle_switch(self):
        self._switched_on = not self._switched_on
        
    def __str__(self):
        return f"{self.__class__.__name__} is {'on' if self._switched_on else 'off'}" 


'''
Child class 1 that inherits from SmartDevice
'''
class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__()
        self._brightness = 50
    
    @property
    def brightness(self):
        return self._brightness
   
    @brightness.setter
    def brightness(self, brightness):
        if 1 <= brightness <= 100:
            self._brightness = brightness
        else:
            raise ValueError (f"Unable to update to {brightness}. Brightness must be between 1 and 100.")
        
    def __str__(self):
        return f"{super().__str__()} with a brightness of {self.brightness}"


'''
Child class 2 that inherits from SmartDevice
'''
class SmartOven(SmartDevice):
    def __init__(self):
        super().__init__()
        self._temperature = 150
        
    @property
    def temperature(self):
        return self._temperature
   
    @temperature.setter
    def temperature(self, temperature):
        if 0 <= temperature <= 260:
            self._temperature = temperature
        else:
            raise ValueError(f"Unable to update to {temperature}. Temperature must be between 0 abd 260 degrees Celsius.")
               
    def __str__(self):
        return f"{super().__str__()} with a temperature of {self.temperature} °C"



def test_custom_device():
    light = SmartLight()
    print(light)
    light.toggle_switch()
    print(light)
    light.brightness = 80
    print(light)
  
    try:
        light.brightness = 0
    except ValueError as e:
            print(f"Error: {e}")
                
    except Exception as e:
        print(f"SmartLight Test Failed: {e}")
        
    try:
        light.brightness = 150
    except ValueError as e:
            print(f"Error: {e}")
                
    except Exception as e:
        print(f"SmartLight Test Failed: {e}")
        
    print("\n" + "-" * 70 + "\n")
    
    try:
        oven=SmartOven()
        print(oven)
        oven.toggle_switch()
        print(oven)
        oven.temperature = 200
        print(oven)
        
        try:
            oven.temperature = -5
        except ValueError as e :
            print(f"Error: {e}")
        
        try:
            oven.temperature = 300
        except ValueError as e :
            print(f"Error: {e}")
            
    except Exception as e:
        print(f"SmartOven Test Failed: {e} ")
        
        
    
# Task 3
class SmartHome:
    def __init__(self, max_items=5):
        self.devices = []
        self.max_items = max_items
        
    def add_device(self, device):
        if len (self.devices) < self.max_items:
            self.devices.append(device)
        else:
            raise ValueError(f"Cannot add more devices. Maximum limit of {self.max_items} reached.")
    
    def remove_device(self, index):
        if 0<= index < len(self.devices):
            del self.devices[index]
        else:
            raise IndexError ("Invalid index. Cannot remove device.")
        
    def get_device(self, index):
        if 0 <= index < len(self.devices):
            return self.devices[index]
        else:
            raise IndexError("Ivalid index.Device not found.")
               
    def toggle_device(self,index):
        self.get_device(index).toggle_switch()
        
    def switch_all_on(self):
        for device in self.devices:
            device._switched_on = True
            
    def switch_all_off(self):
        for device in self.devices:
            device._switched_on = False
            
    def update_option(self, index, value):
        device = self.get_device(index)
        if hasattr(device, "brightness") and 1 <= value <= 100:
            device.brightness = value
        elif hasattr(device, "temperature") and 0 <= value <= 260:
            device.temperature = value
        else:
            raise ValueError ("Invalid value for this device.")
        
    def __str__(self):
        return f"SmartHome with {len(self.devices)} device (s):\n" + "\n".join(f"{i + 1}- {device}" for i, device in enumerate(self.devices))
    
    
    
def test_smart_home():    
    home = SmartHome(max_items=5)
    
    plug = SmartPlug(45)
    light = SmartLight()
    oven = SmartOven()
    
    home.add_device(plug)
    home.add_device(light)
    home.add_device(oven)
    
    print("-" * 40)
    print("Initial state of smart home:")
    print("-" * 40)
    print(home)
    
    print("-" * 40)
    print("Toggling first 2 devices:")
    print("-" * 40)
    home.toggle_device(0)
    home.toggle_device(1)
    print(home)
    
    print("-" * 40)
    print("Switching all devices on:")
    print("-" * 40)
    home.switch_all_on()
    print (home)
    
    print("-" * 40)
    print("Switching all devices off:")
    print("-" * 40)
    home.switch_all_off()
    print(home)
    
    print("-" * 40)
    print("Updating options for the light and oven objects:")
    print("-" * 40)
    home.update_option(1, 75)
    home.update_option(2,200)
    print (home)
    
    print("-" * 40)
    print("Removing second device:")
    print("-" * 40)
    home.remove_device(1)
    print(home)
    
    print("-" * 40)
    print("Trying to add 4 more devices (it should only add 3 more):")
    print("-" * 40)
    try:
        for i in range(4):
            home.add_device(SmartPlug(50))
    except ValueError as e:
        print(f"Error: {e}")
    print(home)
    
    print("-" * 40)
    print("Trying to remove device of invalid index:")
    print("-" * 40)
    try:
        home.remove_device(10)
    except IndexError as e :
        print(f"Error: {e}")
    print(home)
 

'''
Calling test functions for each class
'''
# test_smart_plug()
# test_custom_device()
test_smart_home()
        


    