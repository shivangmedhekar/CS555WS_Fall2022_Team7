# ---------------------------------------------------------------------------- #
#                          US 06: Divorce before death                         #
# ---------------------------------------------------------------------------- #
def divorce_before_death(divorce_date, death_date):
    if not divorce_date or not death_date:
        return True

    if (death_date - divorce_date).days >= 0:
        return True
    else:
        raise Exception("Divorce {} is after death {}".format(str(divorce_date), str(death_date)))