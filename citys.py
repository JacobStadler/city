import random as r
from random import randint as ra
import graphviz as gv
from class_city import City
from enum_choices import *
from class_citizen import Citizen
from city_map import Map
dot = gv.Digraph('Cities')

# my basic idea is that each citizen has a opinion on each of these from 0-1 0 being strong dislike and 1 being strong like.
# basically I will call a routine that will cause them to move if they view another city as more likeable
# some citizens may also prefer lower or higher populace cities

total_amount_of_cities = 20
cities = []
for i in range(total_amount_of_cities):
    cities.append(City(i))

city_neighbors = 10
global failed_n
failed_n = 0

def neighbors(count_cities):
    edges = []
    for i in range(count_cities):
        # [n,e,s,w]
        edges.append([0,1,2,3])
        if i != 0:
            if i == 1:
                random_city = 0
                random_dir = ra(0,3)
            elif i > 1:
                while True:
                    random_city = ra(0,len(edges)-1)
                    print(cities[random_city].readable_neighbors)
                    if len(edges[random_city]) > 0:
                        random_dir = ra(0,len(edges[random_city])-1)
                        if random_city != i and cities[random_city].neighbors[random_dir] == None:
                            break
            
            match edges[random_city][random_dir]:
                case 0:
                    reverse = 2
                case 1:
                    reverse = 3
                case 2:
                    reverse = 0
                case 3:
                    reverse = 1
            
            cities[i].neighbors[reverse] = cities[random_city]
            cities[i].readable_neighbors[reverse] = cities[random_city].name
            cities[random_city].neighbors[random_dir] = cities[i]
            cities[random_city].readable_neighbors[random_dir] = cities[i].name

            dot.edge(f'{cities[random_city].name}',f'{cities[i].name}',dir='both')
            edges[random_city].pop(random_dir)
            edges[i].pop(reverse)

total_amount_of_people = 500*total_amount_of_cities
ppl = []
for i in range(total_amount_of_people):
    ppl.append(Citizen(i))

num_of_ppl = 0
while num_of_ppl < total_amount_of_people:
    city = r.randint(0,total_amount_of_cities-1)
    cities[city].add_citizen(ppl[num_of_ppl])
    ppl[num_of_ppl].occupy = cities[city]
    num_of_ppl += 1

def city_info(c):
    i = 0
    total_aproval = 0
    while i < len(c.residents):
        total_aproval += c.residents[i].like(c)
        i += 1
    string = f'''
    City :          {c.name}\l
    Avg Approval :  {round(total_aproval/len(c.residents),2)}\l
    Pop:            {c.population}\l
    Auth:           {Authority0[c.authority[0]]} {Authority1[c.authority[1]]}\l
    Trade:          {Trade[c.trade]}\l
    Gender Roles:   {GenderRolls[c.genderroles]}\l
    Events :        {Events[c.event]}\l
    Religion :      {Religion[c.religion]}\l
    Caste :         {Caste[c.caste]}\l
    Language :      {Language[c.language]}\l
    Food :          {Food[c.food]}\l
    Art:            {Art[c.art]}\l
    Music :         {Music[c.music]}\l
    Resource :      {Resource[c.resource]}\l
    '''
    return string

for i in range(total_amount_of_cities):
    dot.node(f'{i}',shape="square",label=f'{city_info(cities[i])}')
    #city_info(cities[i])

neighbors(total_amount_of_cities)
#neighbors(total_amount_of_cities)

moves = 1
while moves != 0:
    moves = 0
    civs = total_amount_of_people
    while civs > 0:
        pers = ppl[civs-1]
        civ_like_store = []
        civ_like_score = []
        civ_city = pers.occupy
        civ_like_store.append(pers.occupy)
        civ_like_score.append(pers.like(pers.occupy))
        highest_like = 0
        civ_city_n = len(civ_city.neighbors)
        #print(civ_city_n,civ_like_score)
        i = 0
        while i < civ_city_n:
            if civ_city.neighbors[i] != None:
                civ_like_store.append(civ_city.neighbors[i])
                civ_like_score.append(pers.like(civ_city.neighbors[i]))
                if civ_like_score[i] > civ_like_score[highest_like]:
                    highest_like = i
            else:
                civ_like_store.append(None)
                civ_like_score.append(0)
            i += 1
        if highest_like != 0:
            moves += 1
            #print(f'{pers.id} moved from {civ_city.name} to {civ_city.neighbors[highest_like-1].name}')
            civ_city.rem_citizen(pers)
            civ_city.neighbors[highest_like-1].add_citizen(pers)
            pers.add_occupance(civ_city.neighbors[highest_like-1])
        civs -= 1
    print(f'\nmoves : {moves}\n')
    for i in range(total_amount_of_cities):
        cities[i].poll_residence()

for i in range(total_amount_of_cities):
        print(f'{i} : {cities[i].readable_neighbors}')

r_map = Map()
r_map.noise_map()
r_map.make_map(50)
r_map.display()

dot.render(view=True)