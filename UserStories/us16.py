from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict

def all_males_have_same_last_name(fams_id_list: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    

    for fam_id in fams_id_list:

        husb_name = families[fam_id].get_husband()
        hub_nam = str(husb_name).split()
        Last_name = hub_nam[1]

        children = families[fam_id].get_children()

        for child_id in children:
            if(individuals[child_id].get_gender()!='M'):
                child_name = individuals[child_id].get_name()
                chil_nam = str(child_name).split()
                if(Last_name != chil_nam[1]):
                    raise Exception("All male members of a fimily don't have same surname")   
    return True
