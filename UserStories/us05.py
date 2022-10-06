# ---------------------------------------------------------------------------- #
#                         US 05: Marriage before death                         #
# ---------------------------------------------------------------------------- #
def marriage_before_death(marriageDate, deathDate):

    # if the marriage date & death date are empty/null
    if not marriageDate or not deathDate:
        return True

    # if the death date is after the marriage date
    if (deathDate - marriageDate).days >= 0:
        return True

    # if the marriage date is after the death date
    else:
        raise Exception("marriage {} is after death {}".format(str(marriageDate, str(deathDate))))