# ---------------------------------------------------------------------------- #
#                         US 05: Marriage before death                         #
# ---------------------------------------------------------------------------- #
def marriage_before_death(marriageDate, deathDate):
    """
    Marriage should occur before death of either spouse

    Args:
        marriageDate (_type_): _description_
        deathDate (_type_): _description_

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """

    # if the marriage date & death date are empty/null
    if not marriageDate or not deathDate:
        return True

    # if the death date is after the marriage date
    if (deathDate - marriageDate).days >= 0:
        return True

    # if the marriage date is after the death date
    else:
        raise Exception("marriage {} is after death {}".format(str(marriageDate, str(deathDate))))