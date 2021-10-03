
import numpy as np
import random

layers = 11
numsamples = 1000

import matplotlib.pyplot as plt

arr = np.zeros(layers+1)
for i in range(0,numsamples):
    pos = 0
    # Run through layers of pegs
    for j in range(0,layers):
        # Get random true or false
        if bool(random.getrandbits(1)):
            pos += 1
    # Fill the bin below the peg
    arr[pos] += 1
plt.bar(np.arange(0,layers+1)+1,arr)
