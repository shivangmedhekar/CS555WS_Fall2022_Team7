def summary(individuals_table, families_table):
    """
    summary prints and writes to output.txt the PrettyTables of individual and famalilies and 
    also logs or errors and successful runs of user stories.

    Args:

        param1 (PrettyTable): individuals_table: Is a list of class objects Individual
        param2 (PrettyTable): families_table: Is a list of class objects Family
        param3 (list): logs of error and successful runs of user stories
    
    Returns: 
        This functions doesn't return
    """

    print("Indiviudals")
    print(individuals_table)

    print("Families")
    print(families_table)

    print("\nUser Story Logs")

    with open("output.txt", "w") as output_file:
        
        output_file.write("Indiviudals\n")
        output_file.write(str(individuals_table))

        output_file.write("\nFamilies\n")
        output_file.write(str(families_table))
        
        output_file.write("\n\nUser Stories Logs\n")
        # for log in logs:
        #     output_file.write(log)
        #     output_file.write("\n")