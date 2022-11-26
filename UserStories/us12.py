# ---------------------------------------------------------------------------- #
#                          US 12: Parents not too old                          #
# ---------------------------------------------------------------------------- #

from UserStories.helper_functions import difference_in_dates

def age_gap_between_child_and_parents(child_birth_date, father_birth_date, mother_birth_date) -> bool:
    #The age difference between mother and children should be fewer than 60 years, while the age difference 
    #between father and kid should be less than 80 years.
    

    diff_between_mother_n_child = difference_in_dates(start_date = child_birth_date, end_date = mother_birth_date, unit = "years")
    diff_between_father_n_child = difference_in_dates(start_date = child_birth_date, end_date = father_birth_date, unit = "years")
            
    if(diff_between_mother_n_child >= 60):
        raise Exception(f"The age difference between mother and child should be less than 60 years.")
            
    if(diff_between_father_n_child >= 80):
        raise Exception(f"The age difference between father and child should be less than 80 years.")
            
    return True 