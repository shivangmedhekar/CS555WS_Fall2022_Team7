# ---------------------------------------------------------------------------- #
#                               US 22: Unique IDs                              #
# ---------------------------------------------------------------------------- #
def unique_IDs(ind_ids, fam_ids):
    # All individual IDs should be unique and all family IDs should be unique

    if len(ind_ids)!=len(set(ind_ids)) or len(fam_ids)!=len(set(fam_ids)):
        raise Exception('No unique IDs') 
                    
    return True