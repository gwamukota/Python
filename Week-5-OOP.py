class ExtremeSport:
    """Base class for all extreme sports"""
    
    def __init__(self, name, difficulty, equipment_needed):
        self.name = name
        self.difficulty = difficulty  # 1-10 scale
        self.equipment_needed = equipment_needed
        self.participants = []
        
    def add_participant(self, participant):
        """Add a participant to this sport"""
        self.participants.append(participant)
        print(f"{participant} is now participating in {self.name}!")
        
    def perform(self):
        """Base method for performing the sport"""
        print(f"Performing {self.name}")
        
    def describe(self):
        """Describe the sport details"""
        print(f"{self.name}: Difficulty level {self.difficulty}/10")
        print(f"Equipment needed: {', '.join(self.equipment_needed)}")
        print(f"Current participants: {len(self.participants)}")
        
        
class AerialSport(ExtremeSport):
    """Sports performed in the air"""
    
    def __init__(self, name, difficulty, equipment_needed, max_height):
        super().__init__(name, difficulty, equipment_needed)
        self.max_height = max_height  # in meters
        
    def perform(self):
        """Perform the aerial sport"""
        print(f"Soaring through the air in {self.name} at heights up to {self.max_height}m!")
        
    def calculate_risk(self):
        """Calculate risk based on difficulty and height"""
        return (self.difficulty * self.max_height) / 100
        
        
class WaterSport(ExtremeSport):
    """Sports performed in water"""
    
    def __init__(self, name, difficulty, equipment_needed, water_type):
        super().__init__(name, difficulty, equipment_needed)
        self.water_type = water_type  # ocean, river, lake, etc.
        
    def perform(self):
        """Perform the water sport"""
        print(f"Gliding through {self.water_type} waters while {self.name}!")
        
    def check_conditions(self, weather):
        """Check if conditions are suitable"""
        if weather == "stormy" and self.difficulty > 7:
            return "Too dangerous today!"
        return "Conditions acceptable for " + self.name


# Create specific sport instances
skydiving = AerialSport(
    name="Skydiving",
    difficulty=9,
    equipment_needed=["parachute", "jumpsuit", "altimeter"],
    max_height=4000
)

kitesurfing = WaterSport(
    name="Kitesurfing",
    difficulty=7,
    equipment_needed=["kite", "board", "harness"],
    water_type="ocean"
)

# Demonstrate polymorphism
def participate_in_sport(sport):
    """Function that works with any ExtremeSport object"""
    print(f"\n--- {sport.name} Session ---")
    sport.describe()
    sport.perform()
    
# Use polymorphism to call the same methods on different objects
participate_in_sport(skydiving)
participate_in_sport(kitesurfing)

# Demonstrate unique methods
print(f"\nRisk factor for skydiving: {skydiving.calculate_risk()}")
print(f"Kitesurfing conditions check: {kitesurfing.check_conditions('sunny')}")