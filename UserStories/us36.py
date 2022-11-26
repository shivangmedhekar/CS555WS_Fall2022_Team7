# ---------------------------------------------------------------------------- #
#                           US 36: List recent deaths                          #
# ---------------------------------------------------------------------------- #
from Classes.Individual import Individual
from typing import Dict
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def recent_death(individuals: Dict[str, Individual]) -> Dict:
    curr_date = datetime.now().date()
    recent_deaths = {}
    
    for ind_id in individuals:
        death_date = individuals[ind_id].get_death_date()
        
        if death_date:
            
            diff_from_death_date = difference_in_dates(start_date = death_date, end_date = curr_date, unit = "days")
            
            if diff_from_death_date < 30:
                recent_deaths[ind_id] = death_date

    if recent_deaths:
        f = open("output.txt", "a")
        f.write("\nRecent Deaths: \n")
        print("\nRecent Deaths: ")
        for ind_id in recent_deaths:
            print(f"{ind_id}: {recent_deaths[ind_id]}")
            f.write(f"{ind_id}: {recent_deaths[ind_id]}\n")
        f.close()
    return recent_deaths