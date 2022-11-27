from ProjectUtils.parser import parse
from ProjectUtils.tables import get_tables, print_table
from ProjectUtils.config import GEDCOM_FILE

from TestFiles.run_unittest import run_all_tests

def main():
    
    # Parses through the GEDCOM File and returns two dictionaries
    individuals, families = parse(GEDCOM_FILE)
    
    # Generates Pretty Tables from the dictionaries
    individuals_table, families_table = get_tables(individuals, families)
    
    # Prints the Table on console and output.txt file
    print_table(individuals_table, families_table)
    
    # Runs all UserStories on individuals and famalies dictionaries
    run_all_tests()

if __name__=="__main__":
    main()