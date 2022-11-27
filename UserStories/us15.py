# ---------------------------------------------------------------------------- #
#                         US 15: Fewer than 15 siblings                        #
# ---------------------------------------------------------------------------- #
from typing import List

def fewer_than_15_siblings(siblings: List[str]) -> bool:
    """
    There should be fewer than 15 siblings in a family

    Args:
        siblings (List[str]): List of ID's of childrens from Family Class

    Raises:
        Exception: There are more then 15 siblings in a family

    Returns:
        bool: True if exception not raised
    """
    
    if len(siblings) < 15:
        return True
    else:
        raise Exception(f"There should be fewer than 15 siblings in a family | Sibling Count: {len(siblings)}")