from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict

def child_birth_before_parents_death(fams: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    children should not occur before 9 months since marriage and after 9 months of devorce
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
        WifeDeath = individuals[wifeID].get_deathdate()
        HusbDeath = individuals[husbID].get_deathdate()
        childID = families[famID].get_children()

        for child in childID:
            child_birth = individuals[child].get_birthday()

            if ((HusbDeath-child_birth).days < 30*9):
                raise Exception(f"Father death date:{HusbDeath} should be 9 months before Child birth date:{child_birth}")

            if ((WifeDeath-child_birth).days < 0):
                raise Exception(f"Mother death date:{WifeDeath} should be after Child Birth date:{child_birth}")
        
    return True