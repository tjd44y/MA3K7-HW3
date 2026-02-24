import numpy as np
import random
import statistics as stat
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import linregress

def Simulation():
    hat_contents = list(range(1, 2027))

    while len(hat_contents) > 1:
        choices = random.sample(hat_contents, 2)
        hat_contents.remove(choices[0])
        hat_contents.remove(choices[1])
        hat_contents.append(abs(choices[0]-choices[1]))
    return hat_contents[0]

results = []

for _ in range(10000):
    results.append(Simulation())

print(results)
print(stat.mean(results))

counts = Counter(results)  
xs = np.array(sorted(counts.keys())) 
ps = np.array([counts[x] for x in xs]) / len(results)  

plt.figure(figsize=(8, 6))
plt.bar(xs, ps, width=0.9, alpha=0.7, color='darkblue', label="Empirical Probability")

plt.xlabel("Final Value")
plt.ylabel("Probability")
plt.title("Empirical Probability of Final Values")
plt.tight_layout() 

plt.show()
