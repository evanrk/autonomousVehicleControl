from simulator import *
from seeder import Seeder

simulator = Simulator()
seeder = Seeder(simulator, size=10, seed=1234567890)

points = seeder.seed_points()
simulator.add_elements(points)
roads = seeder.seed_roads()
simulator.add_elements(roads)
vehicles = seeder.seed_vehicles()
simulator.add_elements(vehicles)

# run the code using the decorator from simulator.py
@simulator.run
def logic_func(simulator, iterations):
    for point in simulator.points():
        # print(point.vehicles)
        print(point.roads)
    print(f"num points: {len(simulator.points())}") 
    print(f"num roads: {len(simulator.roads())}") 
    print(f"num vehicles: {len(simulator.vehicles())}") # should be empty for now
    print("hi from the logic func")
    return iterations != 1 # amount of time the sim runs for