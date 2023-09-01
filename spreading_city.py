import random as r
from random import randint as ra
import graphviz as gv
from class_city import City
from enum_choices import *
from class_citizen import Citizen
from city_map import Map
import time
dot = gv.Digraph('Cities')

cities = []
cities.append(City(0))

initial_civs = 20
civs = []
for i in range(initial_civs):
    civs.append(Citizen(i))
    civs[i].parents.append([None])
    civs[i].occupy = cities[0]
    cities[0].add_citizen(civs[i])
founder = ra(0,initial_civs-1)
cities[0].founder = civs[founder]
cities[0].initiate_pref()

mdays = 365
myears = 4000
days = 0
years = 0
dead = True
while dead:
    message = ''
    total_died = 0
    for j in range(len(civs)):
        if civs[j].alive:
            hold = civs[j].occupy
            if civs[j].like(hold) <= 20:
                civs[j].found_city(cities)
                message += f'{civs[j].id} founded a city! {civs[j].occupy.name} || prev = {hold.name} like prev = {civs[j].like(hold)}\n'
            if civs[j].age(mdays,years,days) == False:
                message += f'{civs[j].id} died at {civs[j].age_years}\n'
                dead += 1
                total_died += 1
        else:
            dead += 1
            total_died += 1
    if total_died >= len(civs):
        dead = False

    if message != '':
        print(message)
        time.sleep(.5)
    
    print(f'Year: {years} Day: {days} Died: {total_died}')
    if days == mdays:
        days = 0
        if years == myears:
            break
        years += 1
    days += 1
    
