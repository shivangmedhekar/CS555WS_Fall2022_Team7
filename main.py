from Parser.parser import parse
from prettytable import PrettyTable

GEDCOM_FILE = 'GEDCOM_FILES/Stark_Family.ged'

def main():

    

    individuals, families = parse(GEDCOM_FILE)

    individuals_table = PrettyTable()
    individuals_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

    for indID in individuals:

        name, sex, birth, death, famsID, famcID = individuals[indID].get_individual()
        age = individuals[indID].get_age().years
        alive = individuals[indID].is_alive()

        famsID = "NA" if not famsID else famsID
        famcID = "NA" if not famcID else famcID
        
        individuals_table.add_row([indID, name, sex, birth, age, alive, death, famcID, famsID])

    
    families_table = PrettyTable()
    families_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

    for famID in families:

        husbID, wifeID, marriageDate, divorceDate, children = families[famID].get_family()
        husb_name = individuals[husbID].get_name() if husbID else None
        wife_name = individuals[wifeID].get_name() if wifeID else None
        families_table.add_row([famID, marriageDate, divorceDate, husbID, husb_name, wifeID, wife_name, children])

    print("Indiviudals")
    print(individuals_table)

    print("Families")
    print(families_table)

if __name__=="__main__":
    main()