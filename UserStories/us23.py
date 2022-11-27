# ---------------------------------------------------------------------------- #
#                       US 23: Unique name and birth date                      #
# ---------------------------------------------------------------------------- #
from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def unique_name_and_birthdate(ind_ids: List[str], individuals: List[Dict[str, Individual]]) -> bool:
    """
    No more than one individual with the same name and birth date should appear in a GEDCOM file

    Args:
        ind_ids (List[str]): List of ID's of Individuals
        individuals (List[Dict[str, Individual]]): Is a list of class objects Individual

    Raises:
        Exception: If more then 1 person has same name and birth date

    Returns:
        bool: True if exception not raised
    """

    n = len(ind_ids)
    
    for i in range(n-1):
        name1 = individuals[ind_ids[i]].get_name()
        date1 = individuals[ind_ids[i]].get_birth_date()
        for j in range(i+1,n):
            name2 = individuals[ind_ids[j]].get_name()
            date2 = individuals[ind_ids[j]].get_birth_date()
            if (name1 == name2) and (date1 == date2):
                raise Exception("two persons cannot have same name and date of birth")
                  
    return True