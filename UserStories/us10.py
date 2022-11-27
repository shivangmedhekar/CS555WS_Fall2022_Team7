# ---------------------------------------------------------------------------- #
#                           US 10: Marriage after 14                           #
# ---------------------------------------------------------------------------- #
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def marriage_after_14(husb_birth_date: datetime.date, wife_birth_date: datetime.date, marriage_date: datetime.date) -> bool:
    """
    marriage should occur after 14 years

    Args:
        husb_birth_date (datetime.date): Birth date of husband from Individual Class
        wife_birth_date (datetime.date): Birth date of wife from Individual Class
        marriage_date (datetime.date): Marriage Date of husband and wife from Family Class

    Raises:
        Exception: If any of the spouses are not 14 years old during marriage

    Returns:
        bool: True if exception not raised
    """
    wife_marriage_age = difference_in_dates(start_date = wife_birth_date, end_date = marriage_date, unit = "years")
    husb_marriage_age = difference_in_dates(start_date = husb_birth_date, end_date = marriage_date, unit = "years")

    if wife_marriage_age < 14 or husb_marriage_age < 14:
        raise Exception(f"Marriage should be 14 years after birth")
         
    return True