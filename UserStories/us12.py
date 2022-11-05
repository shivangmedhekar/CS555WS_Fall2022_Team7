from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

from dateutil.relativedelta import relativedelta
from UserStories.helper_functions import difference_in_dates

def age_gap_between_child_and_parents(fams: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    The age difference between mother and children should be fewer than 60 years, while the age difference 
    between father and kid should be less than 80 years.
    Args:
        fams (list): list of families in which the individual is a spouse
        individuals (dict): dict of individuals {indID: []}
        families (dict): dict of families {famID: []}
    Returns:
        bool: True if no_bigamy else False
    """
    if len(fams) <= 1:
        return True
    

    for fam_id in fams:

        husb_id = families[fam_id].get_husband()
        wife_id = families[fam_id].get_wife()
        wife_birth_date = individuals[wife_id].get_birth_date()
        husb_birth_date = individuals[husb_id].get_birth_date()
        children = families[fam_id].get_children()

        for child_id in children:
            
            child_birth_date = individuals[child_id].get_birth_date()
            diff_between_mother_n_child = difference_in_dates(start_date = child_birth_date, end_date = wife_birth_date, unit = "years")
            diff_between_father_n_child = difference_in_dates(start_date = child_birth_date, end_date = husb_birth_date, unit = "years")
            
            if(diff_between_mother_n_child >= 60):
                raise Exception(f"The age difference between mother and child should be less than 60 years.")
            
            if(diff_between_father_n_child >= 60):
                raise Exception(f"The age difference between father and child should be less than 80 years.")
        
    return True 