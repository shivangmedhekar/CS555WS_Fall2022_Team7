# ---------------------------------------------------------------------------- #
#                            US 13: Siblings spacing                           #
# ---------------------------------------------------------------------------- #

from dateutil.relativedelta import relativedelta
from Classes.Individual import Individual
from typing import List, Dict
def siblings_spacing(siblings: List[str], individuals: List[Dict[str, Individual]]) -> bool:
    
    if len(siblings) <= 1:
        return True

    birth_dates = []
    for child_id in siblings:
        child_birth_date = individuals[child_id].get_birth_date()
        birth_dates.append(child_birth_date)

    birth_dates.sort()

    for i in range(len(birth_dates) - 1):
        diff = relativedelta(birth_dates[i + 1], birth_dates[i])
        diff_months = (diff.years * 12) + diff.months
        
        if diff_months < 8 and diff.days > 2:
            return False
        
    return True