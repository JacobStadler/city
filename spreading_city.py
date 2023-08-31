import random as r
from random import randint as ra
import graphviz as gv
from class_city import City
from enum_choices import *
from class_citizen import Citizen
from city_map import Map
dot = gv.Digraph('Cities')


cities = []
cities.append(City(0))

initial_civs = 20
civs = []
for i in range(initial_civs):
    civs.append(Citizen(i))
    civs.parents.append([None])
    civs.occupy = cities[0]
    cities[0].add_citizen(civs[i])
founder = ra(0,initial_civs-1)
cities[0].founder = civs[founder]

days = 365
years = 4000
for i in range(years*days):
    for i in range(len(civs)):
        if not civs.is_dead:
            if civs[i].like <= 20:
                civs[i].found_city(cities)
            civs[i].age(days)
