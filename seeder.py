import random
from simulator import Point, Road, Vehicle

def auto_seed(simulator, seed=None, size=20, num_points=None, num_roads=None, num_vehicles=None):
    pass


class Seeder:
    def __init__(self, seed, simulator, size=20):
        self.size = size
        self.seed = seed
        self.simulator = simulator
        self.points = []
        self.roads = []
        self.vehicles = []
        self.num_points = 0
        self.num_roads = 0
        self.num_vehicles = 0
        
        # set the seed
        random.seed(seed)


    def seed_points(self, num_points=None):
        # get the amount of points
        if not num_points:
            num_points = random.randint(10, 20)

        points = []

        allowed_x = [i for i in range(self.size)]
        allowed_y = [i for i in range(self.size)]
        
        for _ in range(num_points):
            print("points loop")
            x = allowed_x[random.randint(0, len(allowed_x))]
            y = allowed_y[random.randint(0, len(allowed_y))]
            points.append(Point(x, y))
        
        self.points = points
        self.num_points = len(points)
        return points

    def seed_roads(self, num_roads=None):
        # get the amount of roads
        if not num_roads:
            max_roads = self.num_points * (self.num_points - 1)
            num_roads = random.randint(max_roads//2, max_roads//1.25)

        roads = []

        # make the roads
        for _ in range(num_roads):
            print("roads loop")
            new_points = self.points[:]
            rand_index = random.randint(0, len(new_points)) # chooses a start point
            start_point = new_points.pop(rand_index) # makes sure the same point cant be chosen twice
            end_point = new_points[random.randint(0, len(new_points))] # chooses an end point
            roads.append(Road(start_point.id, end_point.id, self.simulator))
        
        self.roads = roads
        self.num_roads = len(roads)
        return roads

    def seed_vehicles(self, num_vehicles=None):
        # get the amount of vehicles
        if not num_vehicles:
            num_vehicles = random.randint(self.num_points//2, self.num_points)

        vehicles = []

        for _ in range(num_vehicles):
            continue

        self.vehicles = vehicles
        self.num_vehicles = len(vehicles)
        return vehicles