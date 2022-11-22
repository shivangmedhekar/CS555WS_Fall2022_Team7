from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def correct_gender_for_role(famIDs,families, individuals):


    
    for famID in famIDs:
        husb_id = families[famID].get_husband()
        husb_gender = individuals[husb_id].get_gender()

        wife_id = families[famID].get_wife()
        wife_gender = individuals[wife_id].get_gender()

        if(husb_gender!=str('M') or wife_gender!=str('F')):
            raise Exception("Gender is wrongly declared")
                    
    return True