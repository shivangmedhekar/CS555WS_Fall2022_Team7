from prettytable import PrettyTable

from Classes.Individual import Individual
from Classes.Family import Family

def get_tables(individuals: list[Individual], families: list[Family]) -> tuple[PrettyTable, PrettyTable]:
    """
    getTables makes PrettyTables objects for individuals and famalies

    Args:

        param1 (list): individuals: Is a list of class objects Individual
        param2 (list): families: Is a list of class objects Family
    
    Returns: 
        (PrettyTable, PrettyTable): It returns PrettyTable objects individuals_table and families_table
    """ 

    # ----------------------------- individuals Table ---------------------------- #
    individuals_table = PrettyTable()
    individuals_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

    for ind_id in individuals:

        name, sex, birth, death, fams_id, famc_id = individuals[ind_id].get_individual()

        age = individuals[ind_id].get_age().years
        alive = individuals[ind_id].is_alive()

        fams_id = "NA" if not fams_id else fams_id
        famc_id = "NA" if not famc_id else famc_id
        death = "NA" if not death else death
        
        individuals_table.add_row([ind_id, name, sex, birth, age, alive, death, famc_id, fams_id])

    # ------------------------------ Families Table ------------------------------ #
    families_table = PrettyTable()
    families_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

    for fam_id in families:

        husb_id, wife_id, marriage_date, divorce_date, children = families[fam_id].get_family()
        husb_name = individuals[husb_id].get_name() if husb_id else None
        wife_name = individuals[wife_id].get_name() if wife_id else None
        families_table.add_row([fam_id, marriage_date, divorce_date, husb_id, husb_name, wife_id, wife_name, children])

    return individuals_table, families_table


def print_table(individuals_table: PrettyTable, families_table: PrettyTable):
    """
    It prints to console and output.txt the PrettyTables of individual and famalilies and 
    also logs or errors and successful runs of user stories.

    Args:

        param1 (PrettyTable): individuals_table: Is a list of class objects Individual
        param2 (PrettyTable): families_table: Is a list of class objects Family
        param3 (list): logs of error and successful runs of user stories
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