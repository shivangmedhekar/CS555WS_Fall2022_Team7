from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def child_birth_before_parents_death(fams_id_list: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    Child should be born before death of mother and before 9 months after death of father
    Args:
     IDList (list): a list of families in which the individual is married.
     individuals (dict): individuals dict indID: []
     families (dict): dict of families {famID: []}
    Returns:
        bool: True if no_bigamy else False
    """

    for fam_id in fams_id_list:

        husb_id = families[fam_id].get_husband()
        wife_id = families[fam_id].get_wife()
        wife_death_date = individuals[wife_id].get_death_date()
        husb_death_date = individuals[husb_id].get_death_date()
        
        if not husb_death_date and not wife_death_date:
            return True
        
        children = families[fam_id].get_children()

        for child_id in children:
            child_birth = individuals[child_id].get_birth_date()
            
            
            if husb_death_date:
                no_of_months_difference = difference_in_dates(start_date = husb_death_date, end_date = child_birth, unit = "months")
                if no_of_months_difference > 9:
                    raise Exception(f"Father death date:{husb_death_date} should be 9 months before Child birth date:{child_birth}")

            if wife_death_date:
                no_of_days_difference = difference_in_dates(start_date = child_birth, end_date = wife_death_date, unit = "days")
                if no_of_days_difference < 0:
                    raise Exception(f"Mother death date:{wife_death_date} should be after Child Birth date:{child_birth}")
        
    return True
