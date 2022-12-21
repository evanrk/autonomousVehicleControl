# Controlling autonomous vehicles using repetitive tsp
controlling many autonomous vehicles at once to minimize traffic and distance travel (feat. traveling salesman problem)

How do you effectively move many different vehicles throughout a grid of roads?

This research question is derived from the Traveling Salesman Problem. The traveling salesman problem is a graph theory problem where a traveling salesman, or vehicle, wants to reach every destination in the shortest possible cost, time, or any negative factor. The problem in the TSP is that it is impossible to solve with both 100% accuracy and good efficiency. My research question is an expansion of this problem because what I want to achieve is moving multiple different vehicles to their destinations as efficiently and as accurately as possible. This question interests me because it applies to more self-driving cars, a technology that is on the rise and it can apply to pathfinding in video games.

Setup
To begin investigating this question, a simulator program must be created to run the logic of the algorithms.

I first created four classes for this program: A VehicleHolder class, a Point class, a Road class, and a Vehicle class. The VehicleHolder class is only to save code, it holds the vehicles that are in the VehicleHolder and the id of the VehicleHolder. The Point class and Road class both inherit from the VehicleHolder class because they both need to have the elements that the VehicleHolder class contains. 

Creating the Point class:
class Point(VehicleHolder):
    def __init__(self, x, y):
        super().__init__("point")
        self.x = x
        self.y = y
        self.position = (x, y)
        self.roads = []

This point class has an x value, y value, position value, and the roads that connect to this point. The super() function call creates the VehicleHolder class with the type of point.


Creating the Road class:
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

The road class has a start value, which is the id of the point class that is the starting point of the road; an end value, which is the id of the point that is the endpoint of the road; a speed which is the max speed that the cars can drive on the road; slope_parts is the two parts (rise and run) that make the slope; distance is the distance total distance of the road, calculated by getting the x and y values of the start and end points and using the distance formula.

Creating the Vehicle class:
class Vehicle:
    def __init__(self, point_on_id, destination, simulator):
        self.id = "vehicle:"+str(uuid4())        
        self.point_on_id = point_on_id  # every car must start at a point
        self.destination = destination
        self.road_on = None
        self.moving_to = None # no car can move at start
 
 
        point_on = simulator.reference(point_on_id)
        self.x = point_on.x
        self.y = point_on.y
 
        self.total_moves = 0

The vehicle class has an id, which is in the same format as the id in VehicleHolder; a point_on_id, the id of the point that the vehicle is on; destination, the point that this vehicle wants to go to; road_on, the road that the vehicle is driving on; moving_to, the point that the vehicle is moving to; an x value; y value; and total_moves, the total moves that the vehicle has taken so far.

The Vehicle class has two methods, move_to and move.
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
            road = simulator.reference(road_id)
            print(f"{self.point_on_id}\t\t\t {road.start}")
            print(self.point_on_id == road.start)
            if self.point_on_id == road.start and towards_id == road.end:
                self.road_on = road_id
                self.point_on = None
                self.moving_to = towards_id
                self.moving = True

The move_to method changes the values so that when looking at the vehicle’s values, you can see where the vehicle is going and how it is getting there.

    def move(self, simulator):
        if self.road_on:
            self.total_moves += 1
            self.point_on_id = self.moving_to
            self.moving_to = None
 
            point_on = simulator.reference(self.point_on_id)
            self.x = point_on.x
            self.y = point_on.y
            self.road_on = None
        else:
            raise IndexError("Vehicle not moving")

The move class checks to see if the move that is trying to be made is valid and if it is, it moves the car to the point it was trying to move to. This is a simplified version of what would be created because it works as a prototype. If this (half-working) prototype were to be expanded, this would be the first thing I would change, changing the car from immediate movement to linear motion.

The class created afterward is the total simulator that centralizes all the functionality for the simulation. None of the parts here are useful for this investigation, so I will not go in-depth for them.

In the second file is the seeder. This is the file that seeds the simulator with a random scenario with given constraints such as the number of points, roads, or vehicles. This is the part that broke in my program.

The final file is the main.py file. This file initializes the program and contains the brains of the program. I was not able to complete this part due to the part that broke in the program.

The Solution (Theoretical):
Since I was not able to program the solution due to an error in my program, I will explain how my solution would have worked. 

Within my program, I would have investigated two simplified solutions. 

Solution 1:
The first solution I came up with is the best but least efficient solution. This solution would behave similarly to a web scraper, and before the program starts, the algorithm would scrape from every point to every other point that is connected to that point and repeat this recursively until it repeats a point. It would then save every path to a dictionary, where the key is the final point reached, and then save those dictionaries to a new dictionary, where the key is the starting point. These new indexed pathways would be used to quickly find the quickest path from any point to any point.
Problem with solution 1:
The problem with this solution is that this solution will be very inefficient. It has to calculate n*(n-1) for every point, so n^2*(n-1); it also has to save all these values in storage, making this solution very large and very inefficient. At very large values, this algorithm will be very slow and take up too much space for it to be used.

Solution 2:
The second solution I came up with is not as accurate, but it is much more efficient. This solution is similar to the first solution but with a limit. When the simulation is running, the program would go to every vehicle and go from every path to every next path up to n times, or n depth. After doing this n-depth search, it would choose the shortest path to the point that is closest to the chosen destination and start moving to that point.

Problem with solution 2:
The problem with this solution is obvious, it is not perfect; there will be times when this algorithm will not find the most efficient solution, even though these times would be rare in the real world because roads usually lead in a logical direction.

Conclusion:
In the end, I was able to answer my question in theory, but I was not able to apply my solution to a program due to an error in my code. One thing that surprised me when I was solving my problem was that the faster solution has a similar accuracy (in theory) as the most accurate (and slowest) solution.

There are expansions for both solutions to this problem. The expansion of the first solution is to make sure that multiple vehicles are not overloading the pathways that they are going over. To solve this, a weight value can be given to each road that is determined by the number of cars that are being routed through this road. The second algorithm has two expansions. The first expansion is the same as the expansion of the first algorithm: to factor in the traffic of the vehicles. The second expansion to the second solution is to find the best number n for the depth for each circumstance so that it is fast enough to run within a certain time frame and gets the cars to their destination in the least distance.
