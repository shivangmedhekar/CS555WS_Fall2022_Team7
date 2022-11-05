# ---------------------------------------------------------------------------- #
#                           US 35: List recent births                          #
# ---------------------------------------------------------------------------- #

from Classes.Individual import Individual
from typing import Dict
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def list_recent_births(individuals: Dict[str, Individual]) -> Dict:
    curr_date = datetime.now().date()
    recent_births = {}
    
    for ind_id in individuals:
        birth_date = individuals[ind_id].get_birth_date()
        
        diff_from_birth_date = difference_in_dates(start_date = birth_date, end_date = curr_date, unit = "days")
        
        if diff_from_birth_date < 30:
            recent_births[ind_id] = birth_date

    if recent_births:
        f = open("output.txt", "a")
        
        f.write("\nRecent Births: \n")
        print("\nRecent Births: ")
        for ind_id in recent_births:
            print(f"{ind_id}: {recent_births[ind_id]}")
            f.write(f"{ind_id}: {recent_births[ind_id]}\n")
        f.close()
        
    return recent_births