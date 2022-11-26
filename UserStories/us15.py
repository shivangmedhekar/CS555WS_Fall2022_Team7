# ---------------------------------------------------------------------------- #
#                         US 15: Fewer than 15 siblings                        #
# ---------------------------------------------------------------------------- #
from typing import List

def fewer_than_15_siblings(siblings: List[str]) -> bool:
    """
    There should be fewer than 15 siblings in a family

    Args:
        siblings (List[str]): _description_

    Raises:
        Exception: _description_

    Returns:
        bool: _description_
    """
    
    if len(siblings) < 15:
        return True
    else:
        raise Exception(f"There should be fewer than 15 siblings in a family | Sibling Count: {len(siblings)}")