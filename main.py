# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import math
from asymtoticAnal import algos

import numpy as np


fibAlgo = algos()
basicOperations = []
sequence = []
kforFib = 1

for i in range(kforFib):
    fibAlgo.fibonacci(i)
    basicOperations.append(fibAlgo.getBasicOp())
    fibAlgo.reset()

def fillSequence():
    for i  in range(1, 50, 1):
        sequence.append([math.floor(fibAlgo.fibanacciFormula(i+2)),math.floor(fibAlgo.fibanacciFormula(i+1))])
fillSequence()
plt.plot(sequence, "bo")
plt.show()

print(sequence)







'''            k+1
input_list = [[2, 1],[3, 2], [5, 3], [8, 5], [13, 8], [21, 13], [34, 21], [55, 34], [89,55],[144, 89],[233, 144],[377, 233], [610, 377], [987, 610],[1597, 987], [2854, 1597], [4181, 2584], [6765, 4181], [10946    , 6765], [17711, 10946], [28657, 17711], [46368, 28657], [75025, 46368], [121393, 75025], [196418, 121393],     [317811, 196418]]
'''