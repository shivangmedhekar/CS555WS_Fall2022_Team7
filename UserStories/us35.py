from traceback import print_tb
from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict
from datetime import datetime


def recent_birth(individuals):
    curr_date = datetime.now().date()
    Birth_List = []
    
    for indID in individuals:
        birth_date = individuals[indID].get_birth_date()
        if birth_date:
            if((curr_date - birth_date).days < 30 and (curr_date - birth_date).days > 0):
                Birth_List.append(birth_date)
        else:
            return False

    if Birth_List:
        print(Birth_List)
    return Birth_List