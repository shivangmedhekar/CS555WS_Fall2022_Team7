from datetime import datetime
from dateutil.relativedelta import relativedelta

def dates_before_current_date(date, type):

    if not date and type == "Deathday":
        return True

    if not date and type == "Birthday":
        raise Exception("has no birthday")

    curr_date = datetime.now().date()
    
    if (curr_date - date).days >= 0:
        return True
    else:
        raise Exception("{} occurs in the future".format(str(date)))
    

def birth_before_marriage(birthday, marriageDate):

    if not marriageDate or not birthday:
        return
    
    if (marriageDate - birthday).days >= 0:
        return True
    else:
        raise Exception("Birthday {} is after marriage {}".format(str(birthday, str(marriageDate))))


def less_then_150_years_old(age):

    if not age or type(age) is not int:
        raise ValueError("Age is not type Integer")

    age = int(str(age))
    
    if age < 150:
        return True
    else:
        raise Exception("Greater then 150 years old")

def user_stories(individuals, families):
    
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


