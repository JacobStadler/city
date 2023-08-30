from random import randint as ra
from enum_choices import *
from perlin_noise import PerlinNoise as pn

class Map():
    def __init__(self):
        self.grid = []

    def get_resource(self,x,y):
        return Resource[self.grid[x][y]]
    
    def make_map(self,nodes):
        noise = pn(octaves=10,seed=1)
        # Resource = ['Inland-water', 'Ocean', 'Farmland', 'Lumber', 'Quarry[stone]', 'Mine[ores/gems]', 'Finished Goods', 'Exotics']
        # 1,2,3,4,5,6
        # ocean, inland-water, Farmland, Lumber, Quarry, Mine
        # Fish,   Travel     , Crops,    Lumber, Stone, Ores
        # this list is limited to physical resources
        for i in range(nodes):
            for j in range(nodes):
                self.grid[i].insert(j,noise[i,j])


