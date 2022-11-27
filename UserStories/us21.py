# ---------------------------------------------------------------------------- #
#                        US 21: Correct gender for role                        #
# ---------------------------------------------------------------------------- #
from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def correct_gender_for_role(fam_id: str, individuals: List[Dict[str, Individual]],families: List[Dict[str, Family]]) -> bool:
    """
    Husband in family should be male and wife in family should be female

    Args:
        fam_id (str): Unique ID of family
        individuals (List[Dict[str, Individual]]): Is a list of class objects Individual
        families (List[Dict[str, Family]]): Is a list of class objects Family

    Raises:
        Exception: If husband has gender F or wife has gender M

    Returns:
        bool: True if exception not raised
    """

    husb_id = families[fam_id].get_husband()
    husb_gender = individuals[husb_id].get_gender()

    wife_id = families[fam_id].get_wife() 
    wife_gender = individuals[wife_id].get_gender()

    if(husb_gender!=str('M') or wife_gender!=str('F')):
        raise Exception(f"Gender is wrongly declared | Error ID: {fam_id}")
        
    return True