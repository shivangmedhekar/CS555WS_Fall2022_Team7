# ---------------------------------------------------------------------------- #
#                         US 02: Birth before marriage                         #
# ---------------------------------------------------------------------------- #

from datetime import datetime
def birth_before_marriage(birthday: datetime.date, marriageDate: datetime.date) -> bool:
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

    if not marriageDate and not birthday:
        return True

    if not marriageDate and birthday:
        return True

    if not birthday and marriageDate:
        raise Exception("Has Marriage date but no Birthday")
    
    if (marriageDate - birthday).days >= 0:
        return True
    else:
        raise Exception("Birthday {} is after marriage {}".format(str(birthday, str(marriageDate))))