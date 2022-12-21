from simulator import Simulator
from seeder import Seeder

simulator = Simulator()
seeder = Seeder(simulator, size=10, seed=1234567890)

points = seeder.seed_points()
simulator.add_elements(points)
roads = seeder.seed_roads()
simulator.add_elements(roads)
vehicles = seeder.seed_vehicles()
simulator.add_elements(vehicles)

def route(vehicle, simulator):
    point_on = simulator.reference(vehicle.point_on_id)
    road_to = simulator.reference(point_on.roads[0])
    point_to_id = road_to.end
    vehicle.move_to(point_to_id, road_to.id, simulator)
    
    simulator.elements[vehicle.id] = vehicle

    print(simulator.elements[vehicle.id].road_on)

# run the code using the decorator from simulator.py
@simulator.run
def Update(simulator, iterations):
    print(f"num points: {len(simulator.points())}") 
    print(f"num roads: {len(simulator.roads())}") 
    print(f"num vehicles: {len(simulator.vehicles())}") 

    for vehicle in simulator.vehicles():
        if not vehicle.road_on:
            route(vehicle, simulator)

    return iterations < 10 # amount of time the sim runs for