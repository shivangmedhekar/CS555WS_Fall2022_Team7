# ---------------------------------------------------------------------------- #
#                            US 16: Male last names                            #
# ---------------------------------------------------------------------------- #

from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict

def male_last_names(fam_id, individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:

    husb_id = families[fam_id].get_husband()
    husb_name = individuals[husb_id].get_name()
    family_last_name = husb_name.split()[1]

    children = families[fam_id].get_children()

    for child_id in children:
        if(individuals[child_id].get_gender() == 'M'):
            child_name = individuals[child_id].get_name()
            male_child_last_name = child_name.split()[1]
                
            if(family_last_name != male_child_last_name):
                raise Exception("All male members of a family don't have same last name") 

    return True

