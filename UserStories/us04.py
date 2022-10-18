# ---------------------------------------------------------------------------- #
#                        US 04: Marriage before divorce                        #
# ---------------------------------------------------------------------------- #
def marriage_before_divorce(marriageDate, divorceDate):
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
    if not marriageDate and not divorceDate:
        return True

    if not divorceDate and marriageDate:
        return True

    if not marriageDate and divorceDate:
        raise Exception("Has divorce date but no marriage date")

    
    # if the divorce date is after the marriage date
    if (divorceDate - marriageDate).days >= 0:
        return True

    # if the marriage date is after the divorce date
    else:
        raise Exception("marriage {} is after divorce {}".format(str(marriageDate, str(divorceDate))))