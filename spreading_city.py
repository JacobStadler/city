import random as r
from random import randint as ra
import graphviz as gv
from class_city import City
from enum_choices import *
from class_citizen import Citizen
from city_map import Map
import time
dot = gv.Digraph('Cities')
dot1 = gv.Digraph('Citizens')

cities = []
cities.append(City(0))

initial_civs = 20
civs = []
dead_civs = []
number_of_civs = 0
for i in range(initial_civs):
    civs.append(Citizen(i))
    civs[i].parents.append([None])
    civs[i].occupy = cities[0]
    cities[0].add_citizen(civs[i])
    if civs[i].gender == 0:
        cities[0].boys.append(civs[i])
    else:
        cities[0].girls.append(civs[i])
    number_of_civs += 1
founder = ra(0,initial_civs-1)
cities[0].founder = civs[founder]
cities[0].initiate_pref()

moves = 0
cities_f = 1
mdays = 365
myears = 100
days = 0
years = 0
dead = True
total_died = 0

while dead and years < myears:
    test_pause = False
    city_founded = False
    message = ''
    to_be_popped = []
    for j in range(len(civs)):
        p = civs[j] # person
        p.age(mdays,years,days)
        if p.alive == False:
            #print(f'{p.id} died at {p.age_years}')
            message += f'{p.id} died at {p.age_years}\n'
            p.occupy.rem_citizen(p)
            dead_civs.append(p)
            to_be_popped.append(j)
            # after pop is still broken
            dead += 1
            total_died += 1
        else:
            hold = p.occupy
            if p.like(hold) <= 20:
                p.found_city(cities)
                message += f'{p.id} founded a city! {p.occupy.name} || prev = {hold.name} like prev = {p.like(hold)}\n'
                dot.edge(f'{hold.name}',f'{p.occupy.name}',dir='both')
                city_founded = True
            if p.like(hold) <= 35 and p.like(hold) > 20:
                if len(hold.nond_n) != 0:
                    move_to = -1
                    for n in range(len(hold.nond_n)):
                        if p.like(hold) < p.like(hold.nond_n[n]):
                            move_to = n
                            p.occupy = hold.nond_n[n]
                    
                    if move_to != -1:
                        hold.nond_n[move_to].add_citizen(p)
                        message += f'{p.id} moved from {hold.name} to {p.occupy.name}\n'
                        moves += 1
            
            if p.age_years >= 20:
                p.have_children(civs,number_of_civs)
                if p.had_kid:
                    number_of_civs += 1
                    message += f'{p.id} and {p.is_preg[1].id} had a bby and named it {p.children[len(p.children)-1].id} after being preg for {p.preg_for} days\n'
                    test_pause = True
                    dot1.edge(f'{p.id}',f'{p.children[len(p.children)-1].id}',dir='both')
                    dot1.edge(f'{p.is_preg[1].id}',f'{p.children[len(p.children)-1].id}',dir='both')
                    
                    p.preg_for = 0
                    p.had_kid = False
                    p.is_preg[1].is_banned = False
                    p.is_preg = [False,None]
                #if p.is_preg[0] == True:
                    #message += f'{p.id} is preg with {p.is_preg[1].id}s bby for {p.preg_for}\n' 
    
    #print(len(to_be_popped))
    if len(to_be_popped) > 0:
        for y in range(len(to_be_popped)):
            #print(f'removed {civs[to_be_popped[y]].id}')
            civs.pop(to_be_popped[y])

    if total_died >= len(civs)+len(dead_civs):
        dead = False
    
    if message != '':
        #print(message)
        if test_pause:
            #time.sleep(10)
            print('sleep')
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
    Dead : {len(dead_civs)}
    Civs : {len(civs)}
    Cities Founded : {cities_f}
    Moves : {moves}''')

dot.render(view=True)
#dot1.render(view=True)