from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def unique_IDs(famIDs,indIDs):

    if len(famIDs)!=len(set(famIDs)) or len(indIDs)!=len(set(indIDs)):
        raise Exception('No unique IDs') 
                    
    return True