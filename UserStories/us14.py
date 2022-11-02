# ---------------------------------------------------------------------------- #
#                          US 14: Multiple births <= 5                         #
# ---------------------------------------------------------------------------- #

from Classes.Family import Family
from Classes.Individual import Individual
from collections import Counter
from typing import List, Dict

def multiple_births_less_then_equal_to_5(fams_id_list: List[str], individuals: List[Dict[str, Individual]],
                                         families: List[Dict[str, Family]]) -> bool:
    
    for fam_id in fams_id_list:

        children = families[fam_id].get_children()
        if len(children):
            
            children_birth_dates = [individuals[child].get_birth_date() for child in children]
            birth_dates_count = dict(Counter(children_birth_dates))
            
            for count in birth_dates_count.values():
                if count > 5:
                    raise Exception("No more than 5 children to a family at a same time")
                
    return True