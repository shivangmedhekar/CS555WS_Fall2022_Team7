# ---------------------------------------------------------------------------- #
#                          US 06: Divorce before death                         #
# ---------------------------------------------------------------------------- #
from datetime import datetime
from UserStories.helper_functions import difference_in_dates
def divorce_before_death(divorce_date: datetime.date, death_date: datetime.date) -> bool:
    """
    Divorce can only occur before death of both spouses

    Args:
        divorce_date (datetime.date): _description_
        death_date (datetime.date): _description_

    Raises:
        Exception: _description_

    Returns:
        bool: _description_
    """
    if not divorce_date or not death_date:
        return True
    
    no_of_days_differnece = difference_in_dates(start_date = divorce_date, end_date = death_date, unit = 'days')
    

    if no_of_days_differnece >= 0:
        return True
    else:
        raise Exception("Divorce {} is after death {}".format(str(divorce_date), str(death_date)))