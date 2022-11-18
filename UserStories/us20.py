# ---------------------------------------------------------------------------- #
#       US 20: Aunts and uncles should not marry their nieces or nephews       #
# ---------------------------------------------------------------------------- #

from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def aunts_and_uncles(family, individuals, famalies):
    
    auncles = famalies[family].get_children()
        
    for i in range(len(auncles)):
        fams_id = individuals[auncles[i]].get_fams_id()
        
        for fam_id in fams_id:
            children = famalies[fam_id].get_children()
                
            for j in range(len(auncles)):

                if i == j:
                    continue
                else:
                    fams_id = individuals[auncles[j]].get_fams_id()
                        
                    for id in fams_id:
                        if id in children:
                            raise Exception("Aunts and uncles should not marry their nieces or nephews")
                    
    return True