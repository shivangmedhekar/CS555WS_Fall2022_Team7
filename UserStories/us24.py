# ---------------------------------------------------------------------------- #
#                       US 24: Unique families by spouses                      #
# ---------------------------------------------------------------------------- #
from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def unique_families_by_spouces(individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    """
    No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file

    Args:
        individuals (List[Dict[str, Individual]]): Is a list of class objects Individual
        families (List[Dict[str, Family]]): Is a list of class objects Family

    Raises:
        Exception: If same spouse details(name, marriage_date) repeat

    Returns:
        bool: True if exception not raised
    """
    
    counter = 0 
    
    duplicate_checker = []
    for fam_id in families:
        
        husb_id = families[fam_id].get_husband()
        wife_id = families[fam_id].get_wife()
        
        husband_name = individuals[husb_id].get_name()
        wife_name = individuals[wife_id].get_name()
        marriage_date = families[fam_id].get_marriage_date()
        
        if not any(x.get('husband_name', '') == husband_name and
                   x.get('wife_name', '') == wife_name and 
                   x.get('marriage_date', '') == marriage_date 
                   for x in duplicate_checker):
            duplicate_checker.append({'husband_name': husband_name, 'wife_name': wife_name,
                                      'marriage_date': marriage_date})
        
        else:
            counter += 1
            
        if counter > 0:
            raise Exception('No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file')
        
        
    return True
        
    
    # for i in range(n-1):
    #     husb1 = families[famIDs[i]].get_husband()
    #     wife1 = families[famIDs[i]].get_wife()
    #     for j in range(i+1,n):
    #         husb2 = families[famIDs[j]].get_husband()
    #         wife2 = families[famIDs[j]].get_wife()
    #         if (husb1 == husb2) and (wife1 == wife2):
    #             raise Exception("Same couple have two families")
                  
    # return True