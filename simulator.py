from uuid import uuid4
import math
import random
"""
Everything outside of the simulator works with ids; to access anything you have to go reference the simulator. This basically simulates pointers for python
the Simulator class ends up being a reference for every variable
"""

# used as a parent class for Point and Road
class VehicleHolder:
    def __init__(self, type):
        self.id = type+":"+str(uuid4()) # so i can access every item easily
        self.vehicles = [] # the vehicles at this point/road

# the vertices of the graph
class Point(VehicleHolder):
    def __init__(self, x, y):
        super().__init__("point")
        self.x = x
        self.y = y
        self.position = (x, y)
        self.roads = []

    
# the vehicle, which follows the graph
class Vehicle:
    def __init__(self, point_on_id, destination, simulator):
        self.id = "vehicle:"+str(uuid4())        
        self.point_on_id = point_on_id  # every car must start at a point
        self.destination = destination
        self.roadOn = None
        self.movingFrom = None # no car can move at start
        self.movingTo = None # no car can move at start

        point_on = simulator.reference(point_on_id)
        self.x = point_on.x
        self.y = point_on.y
        self.position = (self.x, self.y)
    
    def move(self, simulator): # NEED TO FIX
        """Moves the vehicle in its direction
        
        move arguments:
        simulator -- the simulator the vehicle is in
        Return: (if the vehicle is at the station, self.x, self.y, endPoint.y)
        """
        
        if self.roadOn:
            endPoint = simulator.reference(self.movingTo)
            rise, run = simulator.reference(self.roadOn).slope_parts
            slope = rise / run # lol
            
            # change x by one unit and y by slope units
            x_move = run/abs(run) # -1 or 1
            y_move = slope * x_move # -slope or slope
            
            # moves the vehicle
            self.x += x_move
            self.y += y_move
            self.position = (self.x, self.y)
            
        else:
            raise IndexError("VehicleNotMoving")
        
        return (((self.x + x_move) == endPoint.x), self.x, self.y, endPoint.y) # returns important values and if the vehicle is at the destination
        

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
                self.roadOn = road_id
                self.movingFrom = self.point_on
                self.point_on = None
                self.movingTo = towards_id

# the edges of the graph
class Road(VehicleHolder):
    def __init__(self, start_id, end_id, simulator, speed=0): # add curved roads?
        super().__init__("road")
        self.start = start_id
        self.end = end_id
        self.speed = speed # might not be needed

        start_x, start_y = simulator.reference(start_id).position
        end_x, end_y = simulator.reference(end_id).position
        
        self.slope_parts = ((end_y - start_y), (end_x - start_x)) # the slope is used for moving the vehicle
        self.distance = math.sqrt(abs(end_y - start_y) + abs(end_x - start_x)) # pythagorean theorem
        
class Simulator:
    def __init__(self):
        self.iterations = 1
        # self.points = []
        # self.roads = []
        # self.vehicles = []

        self.elements = {}
        self.element_ids = {}


    def points(self):
        points = []
        for id, element in self.elements.items():
            type = id.split(":")[0]
            if type == "point":
                points.append(element)
        return points
    
    def roads(self):
        roads = []
        for id, element in self.elements.items():
            type = id.split(":")[0]
            if type == "road":
                roads.append(element)
        return roads

    def vehicles(self):
        vehicles = []
        for id, element in self.elements.items():
            type = id.split(":")[0]
            if type == "vehicle":
                vehicles.append(element)
        return vehicles
                

    def add_elements(self, elements):
        """adds an element to the simulator
        
        add_element arguments:
        element -- the element being added
        Return: None
        """
        element_ids = list(self.element_ids)
        for element in elements:
            if not (element.id in self.element_ids):
                self.elements[element.id] = element
                element_ids.append(element.id)
                # type = element.id.split(":")[0]
                # if type == "point":
                #     self.points.append(element)
                # elif type == "road":
                #     self.roads.append(element)
                # elif type == "vehicle":
                #     self.vehicles.append(element)
                # else:
                #     raise TypeError("Wrong type")
                
            else:
                raise IndexError(f"RepeatValue {element.id}")
            self.element_ids = set(element_ids)
        


    def reference(self, id):
        """gets the element that corresponds to the id
        
        reference arguments:
        id -- the element id
        Return: the element
        """  
        
        if id in self.element_ids:
            return self.elements[id]
        raise IndexError("NonePointer")
    
    def run(self, call_func=None):
        """Game loop for the simulator
        
        Keyword arguments:
        call_func -- the function the simulator runs, the simulator passes the elements of the simulator and the amount of times it has run. if nothing is given, a function is created by the simulator (FUNCTION MUST RETURN A VALUE VERY TIME IT IS RAN AND TELL THE SIMULATOR WHEN IT ENDS)
        Return: nothing, only prints
        """    
        gameOn = True

        def decorator(func):
            return func(self, self.iterations)

        while gameOn:
            gameOn = decorator(call_func)

            self.iterations += 1
    
    def edit_point(self, id, x=None, y=None, add_road=None, add_vehicle=None):
        type = id.split(":")[0]
        if type != "point":
            raise TypeError("Type is not a point lmao")
        else:
            point = self.reference(id)
            if x:
                point.x = x
            if y:
                point.y = y
            if add_road:
                point.roads.append(add_road)
            if add_vehicle:
                point.vehicles.append(add_vehicle)
            
            # replace the old point with the updated point
            self.elements[id] = point
            # print(self.elements[id].vehicles)
    
    def add_vehicle(self, id, vehicle_id):
        type = id.split(":")[0]
        if type not in ("point", "road"):
            raise TypeError("Type is not a point or a road smh")
        else:
            vehicle_holder = self.reference(id)
            vehicle_holder.vehicles.append(vehicle_id)
            
            # add replace the old vehicle holder element with the updated one
            self.elements[id] = vehicle_holder
