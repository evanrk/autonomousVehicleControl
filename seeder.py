import random
from simulator import *
import math

class Seeder:
    def __init__(self, simulator, size=20, seed=None):
        random.seed(seed)
        self.size = size
        self.simulator = simulator
        self.points = []
        self.roads = []
        self.vehicles = []

    def seed_points(self, num_points=None):
        # get the amount of points
        if not num_points:
            num_points = random.randint(math.ceil(self.size/2), self.size)
        
        # make the points
        allowed_x = list(range(self.size+1))
        allowed_y = list(range(self.size+1))
        for _ in range(num_points):
            x = allowed_x[random.randint(0, len(allowed_x)-1)]
            y = allowed_y[random.randint(0, len(allowed_y)-1)]
            self.points.append(Point(x, y))
        
        return self.points


    def seed_roads(self, num_roads=None):
         # get the amount of roads
        if not num_roads:
            num_points = len(self.points)
            max_roads = num_points * (num_points - 1) - num_points + 1
            num_roads = random.randint(max_roads//2, max_roads//1.25) 
        
        # every point must have one road + 1 extra, at least
        for index in range(num_points):
            new_points = self.points[:]
            
            start_point_id = new_points.pop(index).id # same point cant be chosen twice
            end_point_id = new_points[random.randint(0, len(new_points)-1)].id # end point
            
            road = Road(start_point_id, end_point_id, self.simulator)

            self.roads.append(road)

            self.simulator.add_elements([road])

            self.simulator.edit_point(start_point_id, add_road=road.id) # update the start point of the road
            self.simulator.edit_point(end_point_id, add_road=road.id) # update the end point of the road
            self.roads.append(road)

        # make the roads
        for _ in range(num_roads):
            new_points = self.points[:]
            rand_index = random.randint(0, len(new_points)-1) # chooses a start point
            start_point_id = new_points.pop(rand_index).id # makes sure the same point cant be chosen twice
            end_point_id = new_points[random.randint(0, len(new_points)-1)].id # chooses an end point
            
            road = Road(start_point_id, end_point_id, self.simulator)
            
            self.simulator.add_elements([road])

            self.simulator.edit_point(start_point_id, add_road=road.id) # update the start point of the road
            self.simulator.edit_point(end_point_id, add_road=road.id) # update the end point of the road
            self.roads.append(road)
        return self.roads

    def seed_vehicles(self, num_vehicles=None):
        num_points = len(self.points)

        # get the amount of vehicles
        if not num_vehicles:
            num_vehicles = random.randint(math.ceil(num_points/2), num_points-2)
        
        for _ in range(num_vehicles):
            # creates a duplicate of the points list
            new_points = self.points[:]
            rand_index_on = random.randint(0, len(new_points)-1)
            point_on_id = new_points.pop(rand_index_on).id # no repeats
            
            destination = new_points[random.randint(0, len(new_points)-1)]

            vehicle = Vehicle(point_on_id, destination, self.simulator) # has to be instantiated to get id
            
            # updates the vehicle and adds the vehicle to the seeders vehicles list
            self.simulator.add_elements([vehicle])
            self.simulator.add_vehicle(point_on_id, vehicle.id)
            self.vehicles.append(vehicle)
        
        return self.vehicles