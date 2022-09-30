from parser import parse
from prettytable import PrettyTable

GEDCOM_FILE = 'Stark_Family.ged'

def main():

    table = PrettyTable()
    table.field_names = ["ID", "Name", "Gender", "Birthday", "Death"]

    individuals = parse(GEDCOM_FILE)
    for ind in individuals:

        indID, name, sex, birth, death = ind.get_indID(), ind.get_name(), ind.get_gender(), ind.get_birthday(), ind.get_deathday()
        table.add_row([indID, name, sex, birth, death])

    print(table)

if __name__=="__main__":
    main()