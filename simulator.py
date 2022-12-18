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
    def __init__(self, point_id, simulator):
        self.id = "vehicle:"+uuid4()
        point_on = simulator.reference(point_id)
        self.x = point_on.x
        self.y = point_on.y
        self.position = (point_on.x, point_on.y)
        self.point_on_id = point_id  # every car must start at a point
        self.roadOn = None
        self.movingFrom = None # no car can move at start
        self.movingTo = None # no car can move at start
    
    def move(self):
        """Moves the vehicle in its direction
        
        move arguments:
        Return: None
        """
        

    def move_to(self, towards_id, road_id, simulator): # static function 
        """sets a destination for the vehicle
        
        move_to arguments:
        towards_id -- the id of the Point that the vehicle is moving towards
        road_id -- the id of the Road the point is using
        simulator -- the simulator the vehicle is in
        Return: None
        """
        

        # check if roads used lead to point
        if road_id in simulator.element_ids:
            road = simulator.reference(id)
            if self.point_on_id == road.start and towards_id == road.end:
                self.roadOn = None
                self.movingTo = self.point_on
                self.point_on = None
                self.movingTo = towards_id

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

        element_ids = []
        for point in points:
            element_ids.append(point.id)
            self.elements[point.id] = point
        for road in roads:
            element_ids.append(road.id)
            self.elements[road.id] = road
        for vehicle in vehicles:
            element_ids.append(vehicle.id)
            self.elements[vehicle.id] = vehicle

        # for checking the existence of elements of the simulation
        self.element_ids = set(element_ids)
        
    def add_element(self, element):
        """adds an element to the simulator
        
        add_element arguments:
        element -- the element being added
        Return: None
        """
        
        if not element.id in self.element_ids:
            self.element_ids[element.id] = element
        raise IndexError("RepeatValue")

    def reference(self, id):
        """gets the element that corresponds to the id
        
        reference arguments:
        id -- the element id
        Return: the element
        """
        
        
        if id in self.element_ids:
            return self.elements[id]
        raise IndexError("NonePointer")