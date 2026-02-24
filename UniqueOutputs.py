import numpy as np
import random
import statistics as stat
import matplotlib.pyplot as plt
from collections import OrderedDict

def Simulation():
    hat_contents = list(range(1, 10))

    while len(hat_contents) > 1:
        choices = random.sample(hat_contents, 2)
        hat_contents.remove(choices[0])
        hat_contents.remove(choices[1])
        hat_contents.append(abs(choices[0] - choices[1]))
    return hat_contents[0]

results = []

for _ in range(10000):
    final_number = Simulation() 
    if final_number not in results:
        results.append(final_number)
    else:
        break

print(results)
