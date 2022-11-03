from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict
from dateutil.relativedelta import relativedelta

def marriage_after_14(fams: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    marriage should occur after 14 years
    Args:
        fams (list): list of families the individual is a spouse
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
        marriage_date = families[fam_id].get_marriage_date()
        if marriage_date == None:
            return True
        
        wife_birth_date = individuals[wife_id].get_birth_date()
        husb_birth_date = individuals[husb_id].get_birth_date()
        
        wife_marriage_age = relativedelta(marriage_date, wife_birth_date).years
        husb_marriage_age = relativedelta(marriage_date, husb_birth_date).years

        if wife_marriage_age < 14 or husb_marriage_age < 14:
            raise Exception(f"Marriage should be 14 years after birth")
        
    return True