from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict
from datetime import datetime

def no_children_without_marriage(fams_id_list: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    children should not occur before 9 months since marriage and after 9 months of devorce
    Args:
        IDList(list): a list of families in which the individual is married.
        individuals (dict): individuals dict indID: []
        families (dict): dict of families {famID: []}
    Returns:
        bool: True if no_children_without_marriage else False
    """

    for fam_id in fams_id_list:

        marriage_date = families[fam_id].get_marriage_date()
        divorce_date = families[fam_id].get_divorce_date()
        children = families[fam_id].get_children()
        
        if not marriage_date or not divorce_date:
            return True

        for child_id in children:
            child_birth = individuals[child_id].get_birth_date()

            if ((child_birth - marriage_date).days > 30 * 9):
                raise Exception(f"Divorce date:{marriage_date} should be 9 months before Child birth date:{child_birth}")

            if ((divorce_date - child_birth).days < 30 * 9):
                raise Exception(f"Divorce date:{marriage_date} should be 9 months before Child Birth date:{child_birth}")
        
    return True
