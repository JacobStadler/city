from random import randint as ra
from enum_choices import *
from perlin_noise import PerlinNoise as pn
import numpy as np
import math

class Map():
    def __init__(self):
        self.grid = []
        self.noise = None
        self.nodes = 0

    def get_resource(self,x,y):
        Geo = ['Ocean','Rivers\Lakes','Desert','Hills','Woods','Mountains']
        return Geo[self.grid[x][y]]
    
    def example_noise_map(self):
        mnoise = pn(octaves=10,seed=1)
        x,y = 50,50
        self.noise = [[mnoise([i/x, j/y]) for j in range(x)]  for i in range(y)]
        #print(min(self.noise))
        for i in range(x):
            for j in range(y):
                self.noise[i][j] = (self.noise[i][j]-np.amin(self.noise))/(np.amax(self.noise) - np.amin(self.noise))

    def make_map(self,nodes):
        self.nodes = nodes
        mnoise = pn(octaves=10)
        x,y = nodes,nodes
        p_min = -math.sqrt(2/4)
        p_max = math.sqrt(2/4)
        self.noise = [[(mnoise([i/x, j/y])-p_min)/(p_max-p_min) for j in range(x)]  for i in range(y)]
        
        # Resource = ['Inland-water', 'Ocean', 'Farmland', 'Lumber', 'Quarry[stone]', 'Mine[ores/gems]', 'Finished Goods', 'Exotics']
        # 1,2,3,4,5,6
        # ocean, inland-water, Farmland, Lumber, Quarry, Mine
        # Fish,   Travel     , Crops,    Lumber, Stone, Ores
        # this list is limited to physical resources
        for i in range(nodes):
            self.grid.append([])
            for j in range(nodes):
                geo = self.noise[i][j]*7
                go = -1
                if geo >= 0 and geo < 1:
                    go = 0
                if geo >= 1 and geo < 2:
                    go = 1
                if geo >= 2 and geo < 3:
                    go = 2
                if geo >= 3 and geo < 4:
                    go = 3
                if geo >= 4 and geo < 5:
                    go = 4
                if geo >= 5:
                    go = 5 
                self.grid[i].append(go)

    def display(self):
        for i in range(self.nodes):
            print(self.grid[i])