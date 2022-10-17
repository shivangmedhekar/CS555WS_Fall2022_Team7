# ---------------------------------------------------------------------------- #
#                           US 03: Birth before death                          #
# ---------------------------------------------------------------------------- #

from datetime import datetime
def birth_before_death(birth: datetime.date, death: datetime.date) -> bool:
    """
    Birth should occur before death of an individual

    Args:
        birth (datetime.date()): birthday of an individual
        death (datetime.date() or None): death day of an individual, None if he didn't die yet

    Raises:
        ValueError: If death is passed and birth is None
        Exception: If death day is before brith day

    Returns:
        bool: True if birthday is before deathday
    """

    if not death and not birth:
        return True
    if not death and birth:
        return True

    if not birth and death:
        raise ValueError("Has deathday but no birthday")

    if (death - birth).days >= 0:
        return True
    else:
        raise Exception("Birthday {} is after death {}".format(str(birth),str(death)))