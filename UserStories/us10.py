from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

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
    

    for famID in fams:

        husbID = families[famID].get_husband()
        wifeID = families[famID].get_wife()
        marriage = families[famID].get_marriage_date()
        wifeBirth = individuals[wifeID].get_birthdate()
        husbBirth = individuals[husbID].get_children()

        if((marriage-wifeBirth).days < 14 or (marriage-husbBirth).days < 14):
            raise Exception(f"marriage should be 14 years after birth")
        
    return True