from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict
from datetime import datetime

def recent_death(individuals):
    curr_date = datetime.now().date()
    Death_List = []
    
    for indID in individuals:
        death_date = individuals[indID].get_death_date()
        if death_date:
            if((curr_date - death_date).days < 30 and (curr_date - death_date).days > 0):
                Death_List.append(death_date)

    if Death_List:
        print(Death_List)
    return Death_List