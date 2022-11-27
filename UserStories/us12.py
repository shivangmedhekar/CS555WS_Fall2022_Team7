# ---------------------------------------------------------------------------- #
#                          US 12: Parents not too old                          #
# ---------------------------------------------------------------------------- #
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def age_gap_between_child_and_parents(child_birth_date: datetime.date, father_birth_date: datetime.date,
                                      mother_birth_date: datetime.date) -> bool:
    """
    The age difference between mother and children should be fewer than 60 years, while the age difference 
    between father and kid should be less than 80 years.

    Args:
        child_birth_date (datetime.date): Birth date of child from Individual Class
        father_birth_date (datetime.date): Birth date of father from Individual Class
        mother_birth_date (datetime.date): Birth date of mother from Individual Class

    Raises:
        Exception: The age difference between mother and child is more than 60 years.
        Exception: The age difference between father and child is more than 80 years.

    Returns:
        bool: True if exception not raised
    """

    diff_between_mother_n_child = difference_in_dates(start_date = mother_birth_date, end_date = child_birth_date, unit = "years")
    diff_between_father_n_child = difference_in_dates(start_date = father_birth_date, end_date = child_birth_date, unit = "years")
            
    if(diff_between_mother_n_child >= 60):
        raise Exception(f"The age difference between mother and child should be less than 60 years.")
            
    if(diff_between_father_n_child >= 80):
        raise Exception(f"The age difference between father and child should be less than 80 years.")
            
    return True 