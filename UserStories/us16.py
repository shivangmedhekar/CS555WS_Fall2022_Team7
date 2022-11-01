from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict
from datetime import datetime

def recent_death(individuals):
    curr_date = datetime.now().date()
    Death_List = []
    
    for indID in individuals:
        death_date = Individual[indID].get_death_date()
        if (death_date!='NA'):
            if((-death_date+curr_date).days<30 and (-death_date+curr_date).days>0):
                Death_List.append(death_date)
    
    print(Death_List)
    return Death_List