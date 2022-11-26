from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def unique_families_by_spouces(famIDs, families):
    # No more than one family with the same spouses by name and
    # the same marriage date should appear in a GEDCOM file

    n = len(famIDs)
    
    for i in range(n-1):
        husb1 = families[famIDs[i]].get_husband()
        wife1 = families[famIDs[i]].get_wife()
        for j in range(i+1,n):
            husb2 = families[famIDs[j]].get_husband()
            wife2 = families[famIDs[j]].get_wife()
            if (husb1 == husb2) and (wife1 == wife2):
                raise Exception("Same couple have two families")
                  
    return True