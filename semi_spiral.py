import random as r
from random import randint as ra
def ss_neighbor(count_cities):
    edges = []
    for i in range(count_cities):
        edges.append([0,1,2,3])
        if i != 0:
            if i == 1:
                edges[0] = ra(0,3)
                

    print('cute')