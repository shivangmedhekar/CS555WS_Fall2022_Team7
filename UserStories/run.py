from UserStories.user_stories import *

def run_user_stories(individuals, families):
    """
    run_user_stories runs all functions in user_stories.py on individuals and famalies in the GEDCOM file

    Args:

        param1 (list): individuals: Is a list of class objects Individual
        param2 (list): families: Is a list of class objects Family
    
    Returns: 
        (list) logs: It returns list of logs which include erros and successful runs of each user story
    """ 
    
    logs = []
    for indID in individuals:

        name, sex, birth, death, famsID, famcID = individuals[indID].get_individual()

        # ------------------------- Dates Before Current Date ------------------------ #
        us01_error = False
        try:
            dates_before_current_date(birth, type="Birthday")
        except Exception as e:
            us01_error = True
            logs.append("ERROR: INDIVIDUAL: US01: {}: {}".format(indID,e))

        try:
            dates_before_current_date(death, type="Deathday")
        except Exception as e:
            us01_error = True
            logs.append("ERROR: INDIVIDUAL: US01: {}: {}".format(indID,e))

        if not us01_error:
            logs.append("Successful: US01")

        # -------------------------- Less then 150 Years Old ------------------------- #
        us07_error = False
        try:
            less_then_150_years_old(individuals[indID].get_age().years)
        except (Exception, ValueError) as e:
            us07_error = True
            logs.append("ERROR: INDIVIDUAL: US07: {}: {}".format(indID,e))

        if not us07_error:
            logs.append("Successful: US07")

        # ---------------------------- Birth before death ---------------------------- #
        us03_error = False
        try:
            birth_before_death(birth, death)
        except (Exception, ValueError) as e:
            us03_error = True
            logs.append("ERROR: INDIVIDUAL: US03: {}: {}".format(indID,e))

        if not us03_error:
            logs.append("Successful: US03")
        
        # -------------------------- Marriage before divorce ------------------------- #


        # --------------------------- Marriage before death -------------------------- #


        # --------------------------- Divorce before death --------------------------- #
        us06_error = False
        fams = individuals[indID].get_famsID()
        for fam in fams:
            try:
                divorce = families[fam].get_divorce_date()
                divorce_before_death(divorce, death)
            except (Exception, ValueError) as e:
                us06_error = True
                logs.append("ERROR: INDIVIDUAL: US03: {}: {}".format(indID,e))

        if not us06_error:
            logs.append("Successful: US06")
        # -------------------------- Births Before Marriage -------------------------- #
        us02_error = False
        fams = individuals[indID].get_famsID()

        for fam in fams:
            try:
                marriage_date = families[fam].get_marriage_date()
                birth_before_marriage(individuals[indID].get_birthday(), marriage_date)
            except Exception as e:
                us02_error = True
                logs.append("ERROR: INDIVIDUAL: US02: {}: {}".format(indID,e))

        if not us02_error:
            logs.append("Successful: US02")

        return logs