from simulator import *
from seeder import auto_seed

simulator = Simulator([], [], [], seed=1234576890)
# run the code using the decorator from simulator.py
@simulator.run
def logic_func(elements, iterations, simulator):

    print("hi from the logic func")
    return iterations != 10