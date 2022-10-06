# ---------------------------------------------------------------------------- #
#                        US 04: Marriage before divorce                        #
# ---------------------------------------------------------------------------- #
def marriage_before_divorce(marriageDate, divorceDate):

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