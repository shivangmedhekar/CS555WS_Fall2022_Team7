# ---------------------------------------------------------------------------- #
#                        US 07: Less then 150 years old                        #
# ---------------------------------------------------------------------------- #
def less_then_150_years_old(age: int) -> bool:
    """_summary_

    Args:
        age (int): _description_

    Raises:
        ValueError: _description_
        Exception: _description_

    Returns:
        bool: _description_
    """

    if not age:
        return True

    if type(age) is not int:
        raise ValueError("Age is not type Integer")
    
    if age < 150:
        return True
    else:
        raise Exception("Greater then 150 years old")