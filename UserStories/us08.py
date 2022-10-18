from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict
from datetime import datetime

def no_children_without_marriage(IDList: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    children should not occur before 9 months since marriage and after 9 months of devorce
    Args:
        IDList(list): a list of families in which the individual is married.
        individuals (dict): individuals dict indID: []
        families (dict): dict of families {famID: []}
    Returns:
        bool: True if no_children_without_marriage else False
    """

    for ID in IDList:

        marr = families[ID].get_marriage_date()
        marr = datetime(marr).date()
        divo = families[ID].get_divorce_date()
        divo = datetime(divo).date()
        childID = families[ID].get_children()

        for child in childID:
            child_birth = individuals[child].get_birthday()
            child_birth = datetime(child_birth).date()

            if ((child_birth-marr).days > 30*9):
                raise Exception(f"Divorce date:{marr} should be 9 months before Child birth date:{child_birth}")

            if ((divo-child_birth).days < 30*9):
                raise Exception(f"Divorce date:{marr} should be 9 months before Child Birth date:{child_birth}")
        
    return True
