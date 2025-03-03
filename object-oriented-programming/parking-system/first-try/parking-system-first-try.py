from enum import Enum, auto

class VehicleType(Enum):
    REGULAR = auto()
    DISABLED = auto()
    TRUCK = auto()
    
class ParkingLotException(Exception):
    """basic exception"""
    pass

class ParkingSpotTypeError(ParkingLotException):
    """basic exception"""
    pass

class ParkingLotFullException(ParkingLotException):
    """basic exception"""
    pass

class ParkingLot:
    # don't setup anything here because it will be shared by all of the python class instances.
    
    # only setup the fields in the init class
    def __init__(self):
        self.parking_spots = []
    
    def get_number_of_spots(self):
        return len(self.parking_spots)
    
    def get_number_of_taken_spots(self):
        number_of_taken_spots = 0
        
        for ps in self.parking_spots:
            if ps.vehicle:
                number_of_taken_spots += 1
        
        return number_of_taken_spots
        
    def add_parking_spot(self, parking_spot):
        self.parking_spots.append(parking_spot)
        print("Added parking spot")
        
    def park_vehicle(self, vehicle):
        try:
            for ps in self.parking_spots:
                if not ps.vehicle:
                    if vehicle.type == ps.type:
                        ps.vehicle = vehicle
                        print("Parked " + vehicle.owner + "'s Vehicle")
                        return
                    else:
                        raise ParkingSpotTypeError(f"Can't park {vehicle.type} in {ps.type} spot")
            if self.get_number_of_spots() == self.get_number_of_taken_spots():
                raise ParkingLotFullException("No available parking spots of the correct type")
        except ParkingSpotTypeError as e:
            print(e)
        except ParkingLotFullException as e:
            print(e)
        
class ParkingSpot:
    
    def __init__(self, type: VehicleType):
        if not isinstance(type, VehicleType):
            raise TypeError("Vehicle type must be a VehicleType enum")
        self.type = type
        self.vehicle = None
        
    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        
    def remove_vehicle(self):
        self.vehicle = None
        
class Vehicle:
    
    def __init__(self, type: VehicleType, owner):
        if not isinstance(type, VehicleType):
            raise TypeError("Vehicle type must be a VehicleType enum")
        self.owner = owner
        self.type = type
           
    
p1 = ParkingLot()
v1 = Vehicle(VehicleType.REGULAR, "Dave")
v2 = Vehicle(VehicleType.DISABLED, "Bill")

ps1 = ParkingSpot(VehicleType.REGULAR)
p1.add_parking_spot(ps1)
print(p1.get_number_of_spots())

p1.park_vehicle(v1)
p1.park_vehicle(v2)

ps2 = ParkingSpot(VehicleType.REGULAR)
p1.add_parking_spot(ps2)

p1.park_vehicle(v2)



