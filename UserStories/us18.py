# ---------------------------------------------------------------------------- #
#                       US 18: Siblings should not marry                       #
# ---------------------------------------------------------------------------- #
from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def siblings_should_not_marry(siblings: List[str], individuals: List[Dict[str, Individual]],
                              famalies: List[Dict[str, Family]]) -> bool:
    """
    Siblings should not marry one another

    Args:
        siblings (List[str]): List of ID's of childrens from Family Class
        individuals (List[Dict[str, Individual]]): Is a list of class objects Individual
        famalies (List[Dict[str, Family]]): Is a list of class objects Family

    Raises:
        Exception: If siblings are married to each other

    Returns:
        bool: True if exception not raised
    """
    
    if not len(siblings):
        return True
    
    set_fams = set()
    
    for ind_id in siblings:
        child = individuals[ind_id]
        fams_ids = child.get_fams_id()
        
        for fam_id in fams_ids:
            if fam_id not in set_fams:
                set_fams.add(fam_id)
                
            else:
                husb_id = famalies[fam_id].get_husband()
                wife_id = famalies[fam_id].get_wife()
                
                raise Exception(f"siblings {husb_id} and {wife_id} are married")
    
    return True