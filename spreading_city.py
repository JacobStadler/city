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

cities_f = 1
mdays = 365
myears = 1000
days = 0
years = 0
dead = True
while dead and years <= myears:
    test_pause = False
    city_founded = False
    message = ''
    total_died = 0
    for j in range(len(civs)):
        if civs[j].alive:
            hold = civs[j].occupy
            if civs[j].like(hold) <= 20:
                civs[j].found_city(cities)
                message += f'{civs[j].id} founded a city! {civs[j].occupy.name} || prev = {hold.name} like prev = {civs[j].like(hold)}\n'
                city_founded = True
            if civs[j].like(hold) <= 40 and civs[j].like(hold) > 20:
                if len(hold.nond_n) != 0:
                    for n in range(hold.nond_n):
                        civs[j].like_current = civs[j].like(hold)
                        civs[j].consider_move()
            if civs[j].age(mdays,years,days) == False:
                message += f'{civs[j].id} died at {civs[j].age_years}\n'
                dead += 1
                total_died += 1
            
            if civs[j].is_preg[0] == True:
                civs[j].try_for_kid(civs,civs[j].is_preg[1])
                if civs[j].had_kid:
                    message += f'{civs[j].id} and {civs[j].is_preg[1].id} had a bby and named it {civs[j].children[len(civs[j].children)-1].id} after being preg for {civs[j].preg_for} days\n'
                    test_pause = True
                    civs[j].preg_for = 0
                    civs[j].had_kid = False
                    civs[j].is_preg[1].is_banned = False
                    civs[j].is_preg = [False,None]
                else:
                    message += f'{civs[j].id} is preg with {civs[j].is_preg[1].id}s bby for {civs[j].preg_for}\n' 
            elif civs[j].is_banned == False:
                civs[j].find_partner(civs)
        else:
            dead += 1
            total_died += 1
    if total_died >= len(civs):
        dead = False

    if message != '':
        print(message)
        if test_pause:
            time.sleep(10)
        if city_founded:
            cities_f += 1
    
    print(f'Year: {years} Day: {days} Died: {total_died}')
    if days == mdays:
        days = 0
        if years == myears:
            break
        years += 1
    days += 1
    
print(f'''Stats\n
    Civs :{len(civs)}
    Cities Founded : {cities_f}''')