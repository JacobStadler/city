import random as r
import graphviz as gv
from class_city import City
from enum_choices import *
from class_citizen import Citizen
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

# this neighbors is all sort of jacked up and trying to fix it is pointless as I am going to have to make a new one for my next iteration
def neighbors(city):
    global failed_n
    dup_ciy_list = []
    for i in range(total_amount_of_cities):
        dup_ciy_list.append(i)
    dup_ciy_list.pop(city.name)
    added_n = 0
    while added_n < city_neighbors:
        random_city = r.randint(0,total_amount_of_cities-1)
        random_city_t = r.choice(dup_ciy_list)
        #print(f'{cities[random_city]} {city.neighbors}' )
        if cities[random_city_t] not in city.neighbors and cities[random_city_t] != city:
            city.add_neighbor(cities[random_city_t])
            dot.edge(f'{cities[random_city_t].name}',f'{city.name}',dir='both')
            cities[random_city_t].add_neighbor(city)
            dup_ciy_list.pop(random_city_t)
            added_n += 1
        else:
            failed_n += 1
            print(failed_n)

def n_neighbors():
    for i in range(total_amount_of_cities):
        if i != 0:
            cities[i].name

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

for i in range(total_amount_of_cities):
    neighbors(cities[i])

n_neighbors()

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
        i = 0
        while i < civ_city_n:
            civ_like_store.append(civ_city.neighbors[i])
            civ_like_score.append(pers.like(civ_city.neighbors[i]))
            if civ_like_score[i] > civ_like_score[highest_like]:
                highest_like = i
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

dot.render(view=True)