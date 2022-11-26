# ---------------------------------------------------------------------------- #
#                     US 09: Birth before death of parents                     #
# ---------------------------------------------------------------------------- #
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def child_birth_before_parents_death(child_birth_date: datetime.date, father_death_date: datetime.date, mother_death_date: datetime.date) -> bool:
    """
    Child should be born before death of mother and before 9 months after death of father

    Args:
        child_birth_date (datetime.date): _description_
        father_death_date (datetime.date): _description_
        mother_death_date (datetime.date): _description_

    Raises:
        Exception: _description_
        Exception: _description_

    Returns:
        bool: _description_
    """

    if not father_death_date and not mother_death_date:
        return True
        
    if father_death_date:
        no_of_months_difference = difference_in_dates(start_date = father_death_date, end_date = child_birth_date, unit = "months")
        if no_of_months_difference > 9:
            raise Exception(f"Father death date:{father_death_date} should be 9 months before Child birth date:{child_birth_date}")

    if mother_death_date:
        no_of_days_difference = difference_in_dates(start_date = child_birth_date, end_date = mother_death_date, unit = "days")
        if no_of_days_difference < 0:
            raise Exception(f"Mother death date:{mother_death_date} should be after Child Birth date:{child_birth_date}")
            
    return True