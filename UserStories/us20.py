# ---------------------------------------------------------------------------- #
#                            US 20: Aunts and uncles                           #
# ---------------------------------------------------------------------------- #
from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def aunts_and_uncles(family, individuals, famalies):
    # Aunts and uncles should not marry their nieces or nephews
    
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
                        husb_id = famalies[id].get_husband()
                        wife_id = famalies[id].get_wife()
                        if husb_id in children:
                            raise Exception(f"Aunts and uncles should not marry their nieces or nephews | {auncles[j]} married to nephew {husb_id}")
                        if wife_id in children:
                            raise Exception(f"Aunts and uncles should not marry their nieces or nephews | {auncles[j]} married to niece {wife_id}")
                    
    return True