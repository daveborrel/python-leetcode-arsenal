class ParkingLot:
    
    # don't setup anything here because it will be shared by all of the python class instances.
    
    # only setup the fields in the init class
    def __init__(self, levels):
        self.parking_spots = []
        self.levels = levels 
    
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
        
    def park_vehicle(self, vehicle):
        try:
            for ps in self.parking_spots:
                if not ps.vehicle:
                    if vehicle.type == ps.type:
                        ps.vehicle = vehicle
                        break
                    else:
                        raise Exception("Vehicle type does not match")
        except Exception as e:
            print("An error occured: ", e)
        
class ParkingSpot:
    
    def __init__(self, type):
        self.type = type
        self.vehicle = None
        
    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        
    def remove_vehicle(self, vehicle):
        self.vehicle = vehicle
        
class Vehicle:
    
    def __init__(self, type, owner):
        self.owner = owner
        self.type = type
        
    
p1 = ParkingLot(2)
v1 = Vehicle("Regular", "Dave")

ps1 = ParkingSpot("Regular")
p1.add_parking_spot(ps1)



