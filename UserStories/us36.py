# ---------------------------------------------------------------------------- #
#                           US 36: List recent deaths                          #
# ---------------------------------------------------------------------------- #

from Classes.Individual import Individual
from typing import Dict
from datetime import datetime

def recent_death(individuals: Dict[str, Individual]) -> Dict:
    curr_date = datetime.now().date()
    recent_deaths = {}
    
    for ind_id in individuals:
        death_date = individuals[ind_id].get_death_date()
        
        if death_date:
            
            diff_from_death_date = (curr_date - death_date).days
            if diff_from_death_date < 30:
                recent_deaths[ind_id] = death_date

    if recent_deaths:
        print(recent_deaths)
    return recent_deaths