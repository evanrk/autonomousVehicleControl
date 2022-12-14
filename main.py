from uuid import uuid4

# used as a parent class for Point and Road
class VehicleHolder:
    def __init__(self):
        self.vehicles = [] # the vehicles at this point/road
        self.id = uuid4()

# the vertices of the graph
class Point(VehicleHolder):
    def __init__(self, x, y, popularity):
        self.x = x
        self.y = y
        self.position = (x, y)
        self.popularity = popularity # weighted randomness
    
# the vehicle, which follows the graph
class Vehicle:
    def __init__(self, x, y, pointOn ): 
        self.x = x
        self.y = y
        self.position = (x, y)
        self.pointOn = pointOn  # every car must start at a point
        self.movingFrom = None # no car can move at start
        self.movingTo = None # no car can move at start
    
    def moveTo(self, point, roads):
        # check if roads used lead to point
        pass

# the edges of the graph
class Road(VehicleHolder):
    def __init__(self, distance, connection, speed=0):
        VehicleHolder.__init__(self)
        self.distance = distance
        self.connection = connection
        self.speed = speed # might not be needed

