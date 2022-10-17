from Parser.parser import parse
from Summary.tables import getTables

from Summary.summary import summary
from TestFiles.run_unittest import run_all_tests

from config import GEDCOM_FILE

def main():
    
    individuals, families = parse(GEDCOM_FILE)
    
    individuals_table, families_table = getTables(individuals, families)
    
    summary(individuals_table, families_table)
    run_all_tests()

if __name__=="__main__":
    main()