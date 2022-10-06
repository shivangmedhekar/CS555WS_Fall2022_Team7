from datetime import datetime
# ---------------------------------------------------------------------------- #
#                       US 01: Dates before current date                       #
# ---------------------------------------------------------------------------- #
def dates_before_current_date(date, type):
    """
    run_user_stories runs all functions in user_stories.py on individuals and famalies in the GEDCOM file

    Args:

        param1 (list): individuals: Is a list of class objects Individual
        param2 (list): families: Is a list of class objects Family
    
    Returns: 
        (list) logs: It returns list of logs which include erros and successful runs of each user story
        
    """ 
    if not date and (type == "Marriage" or type == "Divorce"):
        return True

    if not date and type == "Deathday":
        return True

    if not date and type == "Birthday":
        raise Exception("has no birthday")

    curr_date = datetime.now().date()
    
    if (curr_date - date).days >= 0:
        return True
    else:
        raise Exception("{} occurs in the future".format(str(date)))