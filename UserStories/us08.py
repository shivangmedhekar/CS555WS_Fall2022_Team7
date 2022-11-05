# ---------------------------------------------------------------------------- #
#                    US 08: Birth before marriage of parents                   #
# ---------------------------------------------------------------------------- #

from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict
from UserStories.helper_functions import difference_in_dates

def birth_before_marriage_of_parents(fams_id_list: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    Children should be born after marriage of parents (and not more than 9 months after their divorce)

    Args:
        fams_id_list (List[str]): List of families in which the individual is married
        individuals (List[Dict[str, Individual]]): _description_
        families (List[Dict[str, Family]]): _description_

    Raises:
        Exception: _description_
        Exception: _description_

    Returns:
        bool: True if children are born after marriage date of their parents else False
    """

    for fam_id in fams_id_list:

        marriage_date = families[fam_id].get_marriage_date()
        divorce_date = families[fam_id].get_divorce_date()
        children = families[fam_id].get_children()
        
        if not marriage_date or not divorce_date:
            return True

        for child_id in children:
            child_birth = individuals[child_id].get_birth_date()
            
            diff_marriage_child = difference_in_dates(start_date = marriage_date, end_date = child_birth, unit = 'days')
            
            if diff_marriage_child >= 0:
                raise Exception(f"Marriage date:{marriage_date} should be 9 months before Child birth date:{child_birth}")
            
            no_of_months_diff_divorce_child = difference_in_dates(start_date = child_birth, end_date = divorce_date, unit = 'months')
            
            if no_of_months_diff_divorce_child < 9:
                raise Exception(f"Divorce date:{divorce_date} should be more than 9 months after Child Birth date:{child_birth}")
        
    return True
