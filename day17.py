
from math import *
from itertools import *
from collections import *

with open('day17.txt') as f:
    for line in f:
        for token in line.split(', '):
            answer = token
            
print(answer)
