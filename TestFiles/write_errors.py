def write_errors(type, user_story, id, error):
    
    error_msg = create_error_msg(type, user_story, id, error)
    
    with open("output.txt", "a") as output_file:
        print(error_msg)
        output_file.write(error_msg)
        output_file.write("\n")
        
def create_error_msg(type, user_story, id, error) -> str:
    if type == "IND":
        type = ""
    elif type == "FAM":
        type = ""
    return f'ERROR: {type}: {user_story}: {id}: {error}'