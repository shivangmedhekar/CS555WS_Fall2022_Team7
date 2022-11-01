from Classes.Family import Family
from Classes.Individual import Individual
from typing import List, Dict

def multiple_babies_more_than_5(fams_id_list: List[str], individuals: List[Dict[str, Individual]], families: List[Dict[str, Family]]) -> bool:
    

    for fam_id in fams_id_list:

        children = families[fam_id].get_children()

        if (len(children)>=5):
            
            for i in range(len(children)-1):
                count = 0
                child1_birth = individuals[children[i]].get_birth_date()
                for j in range(i+1,len(children)):
                    child2_birth = individuals[children[j]].get_birth_date()
                    if (child1_birth == child2_birth):
                        count = count+1

                if (count>=5):
                    raise Exception("No more than 5 children to a family at a same time")
        
    return True