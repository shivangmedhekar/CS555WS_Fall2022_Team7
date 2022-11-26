# ---------------------------------------------------------------------------- #
#                            US 16: Male last names                            #
# ---------------------------------------------------------------------------- #

from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict

def male_last_names(family_last_name, male_child_names) -> bool:
    
    for name in male_child_names:
        male_child_last_name = name.split()[1]
        if(family_last_name != male_child_last_name):
            raise Exception("All male members of a family don't have same last name") 

    return True

