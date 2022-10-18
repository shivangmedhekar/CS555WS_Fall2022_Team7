# ---------------------------------------------------------------------------- #
#                       US 01: Dates before current date                       #
# ---------------------------------------------------------------------------- #

from datetime import datetime
def dates_before_current_date(date: datetime.date, type: str) -> bool: 
    """
    Dates (birth, marriage, divorce, death) should not be after the current date

    Args:
        date (datetime.date): _description_
        type (str): _description_

    Raises:
        Exception: _description_
        Exception: _description_

    Returns:
        bool: _description_
    """
    if not date and (type == "Marriage" or type == "Divorce"):
        return True

    if not date and type == "Deathday":
        return True

    if not date and type == "Birthday":
        raise Exception("has no birthday")

    curr_date = datetime.now().date()
    
    if (curr_date - date).days >= 0:
        return True
    else:
        raise Exception("{} occurs in the future".format(str(date)))