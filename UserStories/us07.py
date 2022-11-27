# ---------------------------------------------------------------------------- #
#                        US 07: Less then 150 years old                        #
# ---------------------------------------------------------------------------- #
def less_then_150_years_old(age: int) -> bool:
    """
    Death should be less than 150 years after birth for dead people, 
    and current date should be less than 150 years after birth for all living people

    Args:
        age (int): The age of individual

    Raises:
        ValueError: If age is not of type int
        Exception: If age is greater then or equal to 150

    Returns:
        bool: True if exceptions not raised
    """

    if not age:
        return True

    if type(age) is not int:
        raise ValueError("Age is not type Integer")
    
    if age < 150:
        return True
    else:
        raise Exception("Greater then 150 years old")