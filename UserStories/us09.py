from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict
from datetime import datetime

def child_birth_before_parents_death(IDList: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    children should not occur before 9 months since marriage and after 9 months of devorce
    Args:
     IDList (list): a list of families in which the individual is married.
     individuals (dict): individuals dict indID: []
     families (dict): dict of families {famID: []}
    Returns:
        bool: True if no_bigamy else False
    """

    for ID in IDList:

        husbID = families[ID].get_husband()
        wifeID = families[ID].get_wife()
        WifeDeath = individuals[wifeID].get_deathday()
        WifeDeath = datetime(WifeDeath).date()
        HusbDeath = individuals[husbID].get_deathday()
        HusbDeath = datetime(HusbDeath).date()
        childID = families[ID].get_children()

        for child in childID:
            child_birth = individuals[child].get_birthday()
            child_birth = datetime(child_birth).date()

            if ((HusbDeath-child_birth).days < 30*9):
                raise Exception(f"Father death date:{HusbDeath} should be 9 months before Child birth date:{child_birth}")

            if ((WifeDeath-child_birth).days < 0):
                raise Exception(f"Mother death date:{WifeDeath} should be after Child Birth date:{child_birth}")
        
    return True
