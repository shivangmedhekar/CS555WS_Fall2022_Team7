# ---------------------------------------------------------------------------- #
#                        US 04: Marriage before divorce                        #
# ---------------------------------------------------------------------------- #
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def marriage_before_divorce(marriage_date: datetime.date, divorce_date: datetime.date) -> bool:
    """
    Marriage should occur before divorce of spouses, and divorce can only occur after marriage

    Args:
        marriage_date (datetime.date): Marriage date from Family class
        divorce_date (datetime.date): Divorce date from Family class

    Raises:
        Exception: If marriage_date is None and divorce_date is present
        Exception: If marriage_date is after divorce_date

    Returns:
        bool: True if exceptions not raised
    """

    # if the marriage date & divorce date are empty/null
    if not marriage_date and not divorce_date:
        return True

    if not divorce_date and marriage_date:
        return True

    if not marriage_date and divorce_date:
        raise Exception("Has divorce date but no marriage date")

    no_of_days_differnece = difference_in_dates(start_date = marriage_date, end_date = divorce_date, unit = 'days')
    
    # if the divorce date is after the marriage date
    if no_of_days_differnece >= 0:
        return True

    # if the marriage date is after the divorce date
    else:
        raise Exception("marriage {} is after divorce {}".format(str(marriage_date), str(divorce_date)))