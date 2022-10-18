# ---------------------------------------------------------------------------- #
#                            US 13: Siblings spacing                           #
# ---------------------------------------------------------------------------- #

from dateutil.relativedelta import relativedelta
from Classes.Individual import Individual
from typing import List, Dict
def siblings_spacing(siblings: List[str], individuals: List[Dict[str, Individual]]) -> bool:
    
    if len(siblings) <= 1:
        return True

    birthdays = []
    for child in siblings:
        birth = individuals[child].get_birthday()
        birthdays.append(birth)

    birthdays.sort()

    for i in range(len(birthdays) - 1):
        diff = relativedelta(birthdays[i + 1], birthdays[i])
        diff_months = (diff.years * 12) + diff.months
        
        if diff_months < 8 and diff.days > 2:
            return False
        
    return True