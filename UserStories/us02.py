# ---------------------------------------------------------------------------- #
#                         US 02: Birth before marriage                         #
# ---------------------------------------------------------------------------- #

from datetime import datetime
def birth_before_marriage(birth_date: datetime.date, marriage_date: datetime.date) -> bool:
    """
    Birth should occur before marriage of an individual

    Args:
        birth_date (datetime.date): Birth date of an individual
        marriage_date (datetime.date): Marriage date of an individual

    Raises:
        Exception: If an individual has a marriage date but no birth date
        Exception: If an individual has birth date after marriage date

    Returns:
        bool: True only if birth date is before marriage date
    """
    
    if not marriage_date and not birth_date:
        return True

    if not marriage_date and birth_date:
        return True

    if not birth_date and marriage_date:
        raise Exception("Has Marriage date but no Birthday")
    
    if (marriage_date - birth_date).days >= 0:
        return True
    else:
        raise Exception("Birthday {} is after marriage {}".format(str(birth_date, str(marriage_date))))