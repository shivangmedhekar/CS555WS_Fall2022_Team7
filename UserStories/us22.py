def unique_IDs(ind_ids, fam_ids):

    if len(ind_ids)!=len(set(ind_ids)) or len(fam_ids)!=len(set(fam_ids)):
        raise Exception('No unique IDs') 
                    
    return True