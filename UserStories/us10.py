# ---------------------------------------------------------------------------- #
#                           US 10: Marriage after 14                           #
# ---------------------------------------------------------------------------- #
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def marriage_after_14(husb_birth_date: datetime.date, wife_birth_date: datetime.date, marriage_date: datetime.date) -> bool:
    """
    marriage should occur after 14 years

    Args:
        husb_birth_date (datetime.date): _description_
        wife_birth_date (datetime.date): _description_
        marriage_date (datetime.date): _description_

    Raises:
        Exception: _description_

    Returns:
        bool: _description_
    """
    wife_marriage_age = difference_in_dates(start_date = wife_birth_date, end_date = marriage_date, unit = "years")
    husb_marriage_age = difference_in_dates(start_date = husb_birth_date, end_date = marriage_date, unit = "years")

    if wife_marriage_age < 14 or husb_marriage_age < 14:
        raise Exception(f"Marriage should be 14 years after birth")
         
    return True