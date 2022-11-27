# ---------------------------------------------------------------------------- #
#                               US 11: No Bigamy                               #
# ---------------------------------------------------------------------------- #
from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def no_bigamy(fams: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    Marriage should not occur during marriage to another spouse

    Args:
        fams (list): list of families the individual is a spouse
        individuals (dict): dict of individuals {indID: []}
        families (dict): dict of families {famID: []}

    Returns:
        bool: True if exception not raised
    """
    if len(fams) <= 1:
        return True
    
    marriage_count = 0

    for fam_id in fams:

        husb_id = families[fam_id].get_husband()
        wife_id = families[fam_id].get_wife()
        marriage_date = families[fam_id].get_marriage_date()
        divorce_date = families[fam_id].get_divorce_date()

        husband_is_alive = individuals[husb_id].is_alive()
        wife_is_alive = individuals[wife_id].is_alive()
        
        if (marriage_date and not divorce_date) and (husband_is_alive and wife_is_alive):
            marriage_count += 1
        
        if marriage_count > 1:
            raise Exception('has bigamy'.format())
        
    return True