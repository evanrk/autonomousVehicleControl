from simulator import *

simulator = Simulator([], [], [])

# run the code using the decorator from simulator.py
@simulator.run
def logic_func(elements, iterations):
    print("running in the logic func")
    return iterations != 10