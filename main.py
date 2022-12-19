from simulator import *
from seeder import Seeder

simulator = Simulator(seed=1234576890)

seeder = Seeder(simulator.seed, simulator)

# add points
points = seeder.seed_points()
print(points)
simulator.add_elements(points)

# add roads
roads = seeder.seed_roads()
print(roads)
# add vehicles

# simulator.add_elements(points)
# simulator.add_elements(roads)
# simulator.add_elements(vehicles)

# run the code using the decorator from simulator.py
@simulator.run
def logic_func(elements, iterations, simulator):
    print(elements)
    print("hi from the logic func")
    return iterations != 10