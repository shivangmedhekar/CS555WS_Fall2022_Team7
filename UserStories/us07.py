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