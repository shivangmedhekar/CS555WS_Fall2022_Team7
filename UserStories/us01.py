# ---------------------------------------------------------------------------- #
#                       US 01: Dates before current date                       #
# ---------------------------------------------------------------------------- #
from datetime import datetime
from UserStories.helper_functions import difference_in_dates
def dates_before_current_date(date: datetime.date, type: str) -> bool: 
    """
    Dates (birth, marriage, divorce, death) should not be after the current date

    Args:
        date (datetime.date): Any date present in GEDCOM File
        type (str): The type of date being passed

    Raises:
        Exception: If an individual has no birth date
        Exception: If the date is occuring in the future

    Returns:
        bool: True if date doesn't occur in the future
    """
    
    if not date and (type == "Marriage" or type == "Divorce"):
        return True

    if not date and type == "Deathday":
        return True

    if not date and type == "Birthday":
        raise Exception("has no birthday")

    todays_date = datetime.now().date()
    no_of_days_differnece = difference_in_dates(start_date = date, end_date = todays_date, unit = 'days')
    
    if no_of_days_differnece >= 0:
        return True
    else:
        raise Exception("{} occurs in the future".format(str(date)))