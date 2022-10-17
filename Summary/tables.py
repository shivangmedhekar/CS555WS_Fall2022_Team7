from prettytable import PrettyTable

from Classes.Individual import Individual
from Classes.Family import Family

def getTables(individuals: list[Individual], families: list[Family]) -> tuple[PrettyTable, PrettyTable]:
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

    for indID in individuals:

        name, sex, birth, death, famsID, famcID = individuals[indID].get_individual()

        age = individuals[indID].get_age().years
        alive = individuals[indID].is_alive()

        famsID = "NA" if not famsID else famsID
        famcID = "NA" if not famcID else famcID
        
        individuals_table.add_row([indID, name, sex, birth, age, alive, death, famcID, famsID])

    # ------------------------------ Families Table ------------------------------ #
    families_table = PrettyTable()
    families_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

    for famID in families:

        husbID, wifeID, marriageDate, divorceDate, children = families[famID].get_family()
        husb_name = individuals[husbID].get_name() if husbID else None
        wife_name = individuals[wifeID].get_name() if wifeID else None
        families_table.add_row([famID, marriageDate, divorceDate, husbID, husb_name, wifeID, wife_name, children])


    return individuals_table, families_table