class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        
    def move(self):
        """Base movement method"""
        print(f"{self.name} is moving")
        
    def describe(self):
        """Describe the vehicle"""
        print(f"{self.name} (max speed: {self.max_speed} km/h)")


class Car(Vehicle):
    def __init__(self, name, max_speed, num_wheels=4):
        super().__init__(name, max_speed)
        self.num_wheels = num_wheels
        
    def move(self):
        """Car-specific movement"""
        print(f"{self.name} is driving on {self.num_wheels} wheels at {self.max_speed} km/h")
        
    def honk(self):
        """Car-specific method"""
        print(f"{self.name} honks: BEEP BEEP!")


class Plane(Vehicle):
    def __init__(self, name, max_speed, max_altitude):
        super().__init__(name, max_speed)
        self.max_altitude = max_altitude
        
    def move(self):
        """Plane-specific movement"""
        print(f"{self.name} is flying at altitude {self.max_altitude}m")
        
    def land(self):
        """Plane-specific method"""
        print(f"{self.name} is landing on the runway")


class Boat(Vehicle):
    def __init__(self, name, max_speed, boat_type):
        super().__init__(name, max_speed)
        self.boat_type = boat_type
        
    def move(self):
        """Boat-specific movement"""
        print(f"{self.name} is sailing as a {self.boat_type} at {self.max_speed} km/h")
        
    def anchor(self):
        """Boat-specific method"""
        print(f"{self.name} drops anchor")


# Create vehicle instances
sedan = Car(name="Toyota", max_speed=180)
jet = Plane(name="Boeing 747", max_speed=900, max_altitude=12000)
yacht = Boat(name="ferry", max_speed=70, boat_type="yacht")

# Demonstrate polymorphism
def start_journey(vehicle):
    """Function that works with any Vehicle object"""
    print(f"\n--- {vehicle.name} Journey ---")
    vehicle.describe()
    vehicle.move()  # This calls the appropriate move() method based on the object type

# Call the same method on different vehicle types
vehicles = [sedan, jet, yacht]
for vehicle in vehicles:
    start_journey(vehicle)

# Demonstrate unique methods
print("\n--- Vehicle-specific actions ---")
sedan.honk()
jet.land()
yacht.anchor()