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
        bool: True if no_bigamy else False
    """
    if len(fams) <= 1:
        return True
    
    marriage_count = 0

    for famID in fams:

        husbID = families[famID].get_husband()
        wifeID = families[famID].get_wife()
        marriage = families[famID].get_marriage_date()
        divorce = families[famID].get_divorce_date()

        husband_is_alive = individuals[husbID].is_alive()
        wife_is_alive = individuals[wifeID].is_alive()
        
        if (marriage and divorce) and (husband_is_alive and wife_is_alive):
            marriage_count += 1
        
        if marriage_count > 1:
            raise Exception('has bigamy'.format())
        
    return True