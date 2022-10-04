from datetime import datetime
from dateutil.relativedelta import relativedelta

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
    

# ---------------------------------------------------------------------------- #
#                         US 02: Birth before marriage                         #
# ---------------------------------------------------------------------------- #
def birth_before_marriage(birthday, marriageDate):
    """
    birth_before_marriage 

    Args:

        param1 (datetime.date()): birthday: It is a the birthday of a individual
        param2 (datetime.date()): marriageDate: It is the marriage date of the individual from the family table
    
    Returns: 
        (bool) : 
        (Exception)
    """ 

    if not marriageDate and not birthday:
        return True

    if not marriageDate and birthday:
        return True

    if not birthday and marriageDate:
        raise Exception("Has Marriage date but no Birthday")
    
    
    if (marriageDate - birthday).days >= 0:
        return True
    else:
        raise Exception("Birthday {} is after marriage {}".format(str(birthday, str(marriageDate))))


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


# ---------------------------------------------------------------------------- #
#                        US 04: Marriage before divorce                        #
# ---------------------------------------------------------------------------- #
def marriage_before_divorce(marriageDate, divorceDate):

    # if the marriage date & divorce date are empty/null
    if not marriageDate and not divorceDate:
        return True

    if not divorceDate and marriageDate:
        return True

    if not marriageDate and divorceDate:
        raise Exception("Has divorce date but no marriage date")

    
    # if the divorce date is after the marriage date
    if (divorceDate - marriageDate).days >= 0:
        return True

    # if the marriage date is after the divorce date
    else:
        raise Exception("marriage {} is after divorce {}".format(str(marriageDate, str(divorceDate))))


# ---------------------------------------------------------------------------- #
#                         US 05: Marriage before death                         #
# ---------------------------------------------------------------------------- #
def marriage_before_death(marriageDate, deathDate):

    # if the marriage date & death date are empty/null
    if not marriageDate or not deathDate:
        return True


    
    # if the death date is after the marriage date
    if (deathDate - marriageDate).days >= 0:
        return True

    # if the marriage date is after the death date
    else:
        raise Exception("marriage {} is after death {}".format(str(marriageDate, str(deathDate))))


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


# ---------------------------------------------------------------------------- #
#                        US 07: Less then 150 years old                        #
# ---------------------------------------------------------------------------- #
def less_then_150_years_old(age):

    if not age:
        return True

    if type(age) is not int:
        raise ValueError("Age is not type Integer")

    age = int(str(age))
    
    if age < 150:
        return True
    else:
        raise Exception("Greater then 150 years old")
