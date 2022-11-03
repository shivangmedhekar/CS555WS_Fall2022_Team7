# ---------------------------------------------------------------------------- #
#                        US 04: Marriage before divorce                        #
# ---------------------------------------------------------------------------- #

from datetime import datetime
def marriage_before_divorce(marriage_date: datetime.date, divorce_date: datetime.date) -> bool:
    """
    Marriage should occur before divorce of spouses, and divorce can only occur after marriage

    Args:
        marriageDate (datetime.date()): _description_
        divorceDate (datetime.date()): _description_

    Raises:
        Exception: _description_
        Exception: _description_

    Returns:
        _type_: _description_
    """

    # if the marriage date & divorce date are empty/null
    if not marriage_date and not divorce_date:
        return True

    if not divorce_date and marriage_date:
        return True

    if not marriage_date and divorce_date:
        raise Exception("Has divorce date but no marriage date")

    
    # if the divorce date is after the marriage date
    if (divorce_date - marriage_date).days >= 0:
        return True

    # if the marriage date is after the divorce date
    else:
        raise Exception("marriage {} is after divorce {}".format(str(marriage_date, str(divorce_date))))