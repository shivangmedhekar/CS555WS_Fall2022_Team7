# ---------------------------------------------------------------------------- #
#                    US 08: Birth before marriage of parents                   #
# ---------------------------------------------------------------------------- #
from datetime import datetime
from UserStories.helper_functions import difference_in_dates

def birth_before_marriage_of_parents(child_birth_date: datetime.date, marriage_of_parents: datetime.date, divorce_of_parents: datetime.date) -> bool:
    """
    Children should be born after marriage of parents (and not more than 9 months after their divorce)

    Args:
        child_birth_date (datetime.date): Birth date of child from Individual Class
        marriage_of_parents (datetime.date): Marriage date of parents from Family Class
        divorce_of_parents (datetime.date): Divorce date of parents from Family Class

    Raises:
        Exception: If marriage_date is not 9 months before child_birth_date
        Exception: If divorce_date is not 9 months after child_birth_date

    Returns:
        bool: True if exception not raised
    """
    
    diff_marriage_child = difference_in_dates(start_date = marriage_of_parents, end_date = child_birth_date, unit = 'days')
            
    if diff_marriage_child <= 0:
        raise Exception(f"Marriage date:{marriage_of_parents} should be 9 months before Child birth date:{child_birth_date}")
            
    if divorce_of_parents:
        no_of_months_diff_divorce_child = difference_in_dates(start_date = child_birth_date, end_date = divorce_of_parents, unit = 'months')
                
        if no_of_months_diff_divorce_child < 9:
            raise Exception(f"Divorce date:{divorce_of_parents} should be more than 9 months after Child Birth date:{child_birth_date}")
    
    return True