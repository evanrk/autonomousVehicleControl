import random
from simulator import *

def auto_seed(size=20, num_points=None, num_roads=None, num_vehicles=None, seed=None):
    random.seed(seed)
    # get the amount of points
    if not num_points:
        num_points = random.randint(10, 20)
    # get the amount of roads
    if not num_roads:
        max_roads = num_points * (num_points - 1)
        num_roads = random.randint(max_roads//2, max_roads//1.25)
    # get the amount of vehicles
    if not num_vehicles:
        num_vehicles = random.randint(num_points//2, num_points)
    points = []
    roads = []
    vehicles = []

    # make the points
    allowed_x = list(range(size))
    allowed_y = list(range(size))
    for _ in range(num_points):
        x = allowed_x[random.randint(0, len(allowed_x))]
        y = allowed_y[random.randint(0, len(allowed_y))]
        points.append(Point(x, y))

    # make the roads
    for _ in range(num_roads):
        new_points = points[:]
        rand_index = random.randint(0, len(new_points)) # chooses a start point
        start_point = new_points.pop(rand_index) # makes sure the same point cant be chosen twice
        end_point = new_points[random.randint(0, len(new_points))] # chooses an end point
        roads.append(Road(start_point.id, end_point.id, Simulator))

    for _ in range(num_vehicles):
        continue

    print(f"points: {num_points}\nroads: {num_roads}\nvehicles: {num_vehicles}")

    return points, roads, vehicles