# ---------------------------------------------------------------------------- #
#                               US 22: Unique IDs                              #
# ---------------------------------------------------------------------------- #
from typing import List

def unique_IDs(ind_ids: List[str], fam_ids: List[str]) -> bool:
    """
    All individual IDs should be unique and all family IDs should be unique

    Args:
        ind_ids (List[str]): List of ID's of Individuals
        fam_ids (List[str]): List of ID's of Families

    Raises:
        Exception: If duplicate ID is found

    Returns:
        bool: True if exception not raised
    """

    if len(ind_ids)!=len(set(ind_ids)) or len(fam_ids)!=len(set(fam_ids)):
        raise Exception('Duplicate IDs found') 
                    
    return True