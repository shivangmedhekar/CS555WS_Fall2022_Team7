from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict
from datetime import datetime

def child_birth_before_parents_death(IDList: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    Child should be born before death of mother and before 9 months after death of father
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
        HusbDeath = individuals[husbID].get_deathday()
        
        if not HusbDeath or not WifeDeath:
            return True
        
        childID = families[ID].get_children()

        for child in childID:
            child_birth = individuals[child].get_birthday()
            
            
            if ((child_birth - HusbDeath).days > 30*9):
                raise Exception(f"Father death date:{HusbDeath} should be 9 months before Child birth date:{child_birth}")

            if ((WifeDeath-child_birth).days < 0):
                raise Exception(f"Mother death date:{WifeDeath} should be after Child Birth date:{child_birth}")
        
    return True
