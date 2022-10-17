from datetime import datetime

def birth_before_marriage_of_parents(birthdays, marriage):

    if len(birthdays) == 0 or not marriage:
        return None

    errors = []
    for childDate in birthdays:
        # if not date or not marriage:
        #     return None
        if (childDate - marriage).days >= 0:
            pass
        else:
            errors.append("marriage {} is after chidren born {}".format(str(marriage, str(childDate))))

    if len(errors):
        return errors
    else:
        return True