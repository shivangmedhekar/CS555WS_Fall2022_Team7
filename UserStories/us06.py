# ---------------------------------------------------------------------------- #
#                          US 06: Divorce before death                         #
# ---------------------------------------------------------------------------- #
def divorce_before_death(divorce, death):
    if not divorce or not death:
        return True

    if (death - divorce).days >= 0:
        return True
    else:
        raise Exception("Divorce {} is after death {}".format(str(divorce),str(death)))