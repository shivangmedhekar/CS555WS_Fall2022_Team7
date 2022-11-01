from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict
from datetime import datetime


def recent_birth(individuals):
    curr_date = datetime.now().date()
    Birth_List = []
    
    for indID in individuals:
        birth_date = Individual[indID].get_birth_date()
        if (birth_date!='NA'):
            if((-birth_date+curr_date).days<30 and (-birth_date+curr_date).days>0):
                Birth_List.append(birth_date)

    print(Birth_List)
    return Birth_List 