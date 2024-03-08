import random
import matplotlib.pyplot as plt
import numpy as np

counts = np.zeros(11, np.int)
bins = [2,3,4,5,6,7,8,9,10,11,12]

def roll():
    counts[random.randint(1,6) + random.randint(1,6) - 2] += 1

for x in range(1000):
    roll()

print(counts)
plt.bar(bins,counts)    
plt.show()