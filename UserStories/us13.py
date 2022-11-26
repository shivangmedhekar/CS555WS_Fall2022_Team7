# ---------------------------------------------------------------------------- #
#                            US 13: Siblings spacing                           #
# ---------------------------------------------------------------------------- #

from typing import List
from datetime import datetime

from UserStories.helper_functions import difference_in_dates
def siblings_spacing(birth_dates: List[datetime.date]) -> bool:
    """
    Birth dates of siblings should be more than 8 months apart or less than 2 days apart
    (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)

    Args:
        siblings (List[str]): _description_
        individuals (List[Dict[str, Individual]]): _description_

    Returns:c
        bool: _description_
    """
    
    if len(birth_dates) <= 1:
        return True
    
    birth_dates.sort()

    for i in range(len(birth_dates) - 1):
        no_of_days_difference = difference_in_dates(start_date = birth_dates[i], end_date = birth_dates[i + 1], unit = "days")
        no_of_months_difference = difference_in_dates(start_date = birth_dates[i], end_date = birth_dates[i + 1], unit = "months")
        
        if no_of_months_difference < 8 and no_of_days_difference > 2:
            return False
        
    return True