# ---------------------------------------------------------------------------- #
#                     US 25: Unique first names in families                    #
# ---------------------------------------------------------------------------- #

from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def unique_first_names_in_families(children, individuals):
    
    first_names = set()
    birth_dates = set()
    for child in children:
        
        name = individuals[child].get_name()
        first_name, last_name = name.split(' ')
        birth_date = individuals[child].get_birth_date()
        
        if first_name in first_names and birth_date in birth_dates:
            raise Exception("No more than one child with the same name and birth date should appear in a family")

        else:
            first_names.add(first_name)
            birth_dates.add(birth_date)
    
    return True