# ---------------------------------------------------------------------------- #
#                           US 03: Birth before death                          #
# ---------------------------------------------------------------------------- #
def birth_before_death(birth, death):
    if not death and not birth:
        return True
    if not death and birth:
        return True

    if not birth and death:
        raise Exception("Has deathday but no birthday")

    if (death - birth).days >= 0:
        return True
    else:
        raise Exception("Birthday {} is after death {}".format(str(birth),str(death)))