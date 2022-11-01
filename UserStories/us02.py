# ---------------------------------------------------------------------------- #
#                         US 02: Birth before marriage                         #
# ---------------------------------------------------------------------------- #

from datetime import datetime
def birth_before_marriage(birth_date: datetime.date, marriage_date: datetime.date) -> bool:
    """
    Birth should occur before marriage of an individual

    Args:
        birthday (datetime.date): _description_
        marriageDate (datetime.date): _description_

    Raises:
        Exception: _description_
        Exception: _description_

    Returns:
        bool: _description_
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