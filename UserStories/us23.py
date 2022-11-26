from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def unique_name_and_birthdate(indIDs, individual):

    n = len(indIDs)
    
    for i in range(n-1):
        name1 = individual[indIDs[i]].get_name()
        date1 = individual[indIDs[i]].get_birth_date()
        for j in range(i+1,n):
            name2 = individual[indIDs[j]].get_name()
            date2 = individual[indIDs[j]].get_birth_date()
            if (name1 == name2) and (date1 == date2):
                raise Exception("two persons cannot have same name and date of birth")
                  
    return True