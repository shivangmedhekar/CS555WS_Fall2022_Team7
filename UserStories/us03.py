# ---------------------------------------------------------------------------- #
#                           US 03: Birth before death                          #
# ---------------------------------------------------------------------------- #

from datetime import datetime
def birth_before_death(birth_date: datetime.date, death_day: datetime.date) -> bool:
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

    if not death_day and not birth_date:
        return True
    if not death_day and birth_date:
        return True

    if not birth_date and death_day:
        raise ValueError("Has deathday but no birthday")

    if (death_day - birth_date).days >= 0:
        return True
    else:
        raise Exception("Birthday {} is after death {}".format(str(birth_date),str(death_day)))