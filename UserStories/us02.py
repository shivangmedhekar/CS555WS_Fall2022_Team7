# ---------------------------------------------------------------------------- #
#                         US 02: Birth before marriage                         #
# ---------------------------------------------------------------------------- #
def birth_before_marriage(birthday, marriageDate):
    """
    birth_before_marriage 

    Args:

        param1 (datetime.date()): birthday: It is a the birthday of a individual
        param2 (datetime.date()): marriageDate: It is the marriage date of the individual from the family table
    
    Returns: 
        (bool) : 
        (Exception)
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