from uuid import uuid4
"""
Everything outside of the simulator works with ids; to access anything you have to go reference the simulator. This basically simulates pointers for python
the Simulator class ends up being a reference for every variable
"""

# used as a parent class for Point and Road
class VehicleHolder:
    def __init__(self, type):
        self.id = type+":"+uuid4() # so i can access every item easily
        self.vehicles = [] # the vehicles at this point/road

# the vertices of the graph
class Point(VehicleHolder):
    def __init__(self, x, y, popularity):
        super().__init__("point")
        self.x = x
        self.y = y
        self.position = (x, y)
        self.popularity = popularity # weighted randomness
    
# the vehicle, which follows the graph
class Vehicle:
    def __init__(self, pointId, simulator):
        self.id = "vehicle:"+uuid4()
        pointOn = simulator.reference(pointId)
        self.x = pointOn.x
        self.y = pointOn.y
        self.position = (pointOn.x, pointOn.y)
        self.pointOnId = pointId  # every car must start at a point
        self.roadOn = None
        self.movingFrom = None # no car can move at start
        self.movingTo = None # no car can move at start
    
    def moveTo(self, towardsId, roadId, simulator): # static function 
        # check if roads used lead to point
        if roadId in simulator.roadIds:
            road = simulator.reference(id)
            if self.pointOnId == road.start and towardsId == road.end:
                self.roadOn = None
                self.movingTo = self.pointOn
                self.pointOn = None
                self.movingTo = towardsId

# the edges of the graph
class Road(VehicleHolder):
    def __init__(self, startId, endId, speed=0):
        super().__init__("road")
        self.start = startId
        self.end = endId
        self.speed = speed # might not be needed
        self.distance = 0 # need to calculate

        

class Simulator:
    def __init__(self, points, roads, vehicles):
        self.elements = {}

        elementIds = []
        for point in points:
            elementIds.append(point.id)
            self.elements[point.id] = point
        for road in roads:
            elementIds.append(road.id)
            self.elements[road.id] = road
        for vehicle in vehicles:
            elementIds.append(vehicle.id)
            self.elements[vehicle.id] = vehicle

        # for checking the existence of elements of the simulation
        self.elementIds = set(elementIds)
        
    def addElement(self, element):
        if not element.id in self.elementIds:
            self.elementIds[element.id] = element
        raise IndexError("RepeatValue")

    def reference(self, id):
        if id in self.elementIds:
            return self.elements[id]
        raise IndexError("NonePointer")