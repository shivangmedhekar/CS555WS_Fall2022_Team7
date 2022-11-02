# ---------------------------------------------------------------------------- #
#                           US 35: List recent births                          #
# ---------------------------------------------------------------------------- #

from Classes.Individual import Individual
from typing import Dict
from datetime import datetime

def list_recent_births(individuals: Dict[str, Individual]) -> Dict:
    curr_date = datetime.now().date()
    recent_births = {}
    
    for ind_id in individuals:
        birth_date = individuals[ind_id].get_birth_date()
        
        diff_from_birth_date = (curr_date - birth_date).days
        
        if diff_from_birth_date < 30:
            recent_births[ind_id] = birth_date

    if recent_births:
        print(recent_births)
    return recent_births