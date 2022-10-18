from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

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
    

    for famID in fams:

        husbID = families[famID].get_husband()
        wifeID = families[famID].get_wife()
        wifeBirth = individuals[wifeID].get_birthdate()
        husbBirth = individuals[husbID].get_birthdat()
        childID = families[famID].get_children()


        for child in childID:
            childbirth = individuals[child].get_birthday()
            if((wifeBirth-childbirth).days < 365*60):
                raise Exception(f"The age difference between mother and son should be less than 60 years.")
            if((husbBirth-childbirth).days < 365*80):
                raise Exception(f"The age difference between father and son should be less than 80 years.")
        
    return True 