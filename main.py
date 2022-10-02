from Parser.parser import parse
from Summary.tables import getTables
from UserStories.run import run_user_stories
from Summary.summary import summary

GEDCOM_FILE = 'GEDCOM_FILES/Stark_Family.ged'

def main():

    individuals, families = parse(GEDCOM_FILE)

    individuals_table, families_table = getTables(individuals, families)

    logs = run_user_stories(individuals, families)

    summary(individuals_table, families_table, logs)


if __name__=="__main__":
    main()
    