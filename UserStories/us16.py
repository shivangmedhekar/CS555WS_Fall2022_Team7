# ---------------------------------------------------------------------------- #
#                            US 16: Male last names                            #
# ---------------------------------------------------------------------------- #
from typing import List

def male_last_names(family_last_name: str, male_child_names: List[str]) -> bool:
    """
    All male members of a family should have the same last name

    Args:
        family_last_name (str): last name of father from Individual Class
        male_child_names (List[str]): List of names of all children

    Raises:
        Exception: If all children don't have same last name

    Returns:
        bool: True if exception not raised
    """
    
    for name in male_child_names:
        male_child_last_name = name.split()[1]
        if(family_last_name != male_child_last_name):
            raise Exception(f"All male members of a family don't have same last name | Family Last Name: {family_last_name} | Error Name: {name}") 

    return True

