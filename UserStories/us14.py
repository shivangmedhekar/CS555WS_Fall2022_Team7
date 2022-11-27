# ---------------------------------------------------------------------------- #
#                          US 14: Multiple births <= 5                         #
# ---------------------------------------------------------------------------- #

from Classes.Family import Family
from Classes.Individual import Individual
from collections import Counter
from typing import List, Dict
 
def multiple_births_less_then_equal_to_5(children_birth_dates) -> bool:
    """
    No more than five siblings should be born at the same time

    Args:
        children_birth_dates (_type_): List of birth dates

    Raises:
        Exception: If more than 5 birthdates are same

    Returns:
        bool: True if exception not raised
    """
    # 
    
    birth_dates_count = dict(Counter(children_birth_dates))
            
    for count in birth_dates_count.values():
        if count > 5:
            raise Exception("No more than 5 children to a family at a same time")
                
    return True