from datetime import datetime
from functools import lru_cache

from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

# --------------------------------- Constants -------------------------------- #
VALID_TAGS = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR',
              'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
          "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


@lru_cache
def parse(GEDCOM_FILE: str) -> tuple[List[Dict[str, Individual]], List[Dict[str, Family]]]:
    """
    This functions parses through the GEDCOM file and extracts important components from it and
    put it to a list of objects which are Individual and Families

    Args:
        GEDCOM_FILE (str): Location of GEDCOM File

    Returns:
        tuple[List[Dict[str, Individual]], List[Dict[str, Family]]]: Dictionary of Indiviudals and Famalies
    """

    individuals, families = {}, {}
    with open(GEDCOM_FILE, 'r') as file:

        lines = file.readlines()
        i = 0

        while(i < len(lines)):

            level, tag = get_level_n_tag(lines[i])

            # ------------------------- Parse through Individuals ------------------------ #
            if "INDI" == tag:
                indID = lines[i].split('@')[1]
                famcID = []
                famsID = []
                name = None
                sex = None
                birth = None
                death = None

                i = i + 1;
                while("INDI" not in lines[i] and "0 TRLR" not in lines[i]):

                    level, tag = get_level_n_tag(lines[i])

                    if tag not in VALID_TAGS:
                        i = i + 1
                        continue
                    
                    #Parse out the famc id
                    if ("FAMC" == tag and level == "1"):
                        famcID.append(lines[i].split("@")[1])

                    #Parse out the fams id
                    elif ("FAMS" == tag and level == "1"):
                        famsID.append(lines[i].split("@")[1])
                    
                    #Parse out the name
                    elif ("NAME" == tag and level == "1"):
                        name = lines[i][7:len(lines[i]) - 1].replace("/", "").replace("\n", "")
                    
                    #Parse out the sex
                    elif ("SEX" == tag and level == "1"):
                        sex = lines[i][6]

                    #Parse out the birthday
                    elif ("BIRT" == tag and level == "1"):
                        i = i + 1
                        birth = parse_date(lines[i].replace("2 DATE ", ''))

                    #Parse out the deathday
                    elif ("DEAT" == tag and level == "1"):
                        i = i + 1
                        death = parse_date(lines[i].replace("2 DATE ", ''))

                    if ("TRLR" == tag or "FAM" == tag):
                        break

                    i = i + 1
                
                individuals[indID] = Individual(indID, famcID, famsID, name, sex, birth, death)

            # -------------------------- Parse through famalies -------------------------- #
            elif "FAM" == tag:
                famID = lines[i].split("@")[1]
                husband = None
                wife = None
                marriageDate = None
                divorceDate = None
                children = []
                i = i + 1
                while (True):

                    level, tag = get_level_n_tag(lines[i])
                    
                    #Parse out the husband
                    if ("HUSB" == tag and "1" == level):
                        husband = lines[i].split("@")[1]

                    #Parse out the wife
                    elif ("WIFE" == tag and "1" == level):
                        wife = lines[i].split("@")[1]

                    #Parse out the marriage date
                    elif ("MARR" == tag and "1" == level):
                        i = i + 1
                        marriageDate = parse_date(lines[i].replace("2 DATE ", ''))

                    #Parse out the divorce date
                    elif ("DIV" == tag):
                        i = i + 1
                        divorceDate = parse_date(lines[i].replace("2 DATE ", ''))

                    #Parse out the children
                    elif ("CHIL" == tag and "1" == level):
                        children.append(lines[i].split("@")[1])

                    elif ("TRLR" == tag and "0" == level) or ("FAM" == tag):
                        break

                    i = i + 1
                families[famID] = Family(famID, husband, wife, marriageDate, divorceDate, children)

            if "TRLR" == tag and "0" == level:
                break

            if "INDI" not in lines[i] and tag != "FAM":
                i = i + 1
    
    return individuals, families


# ---------------------------------------------------------------------------- #
#                               Helper Functions                               #
# ---------------------------------------------------------------------------- #

def parse_date(date: str) -> datetime.date:
    """
    This function take the format used in GEDCOM files and turns it into datetime format

    Args:
        date (str): Takes date in GEDCOM format in type string

    Returns:
        datetime.date: Parsed date
    """

    try: 
        day, month, year = date.split(" ")
        month = MONTHS.index(month.upper()) + 1
        day, month, year = int(day), int(month), int(year)

        datetime_element = datetime(year, month, day)

        return datetime_element.date()
    except:
        print(f'ERROR! GEDCOM PARSER | Following date could not be passed: {date}')
        return None

def get_level_n_tag(line: str) -> tuple[int, str]:
    """
    This function takes file line of type string and extracts level and tag

    Args:
        line (str): It is file line of type string

    Returns:
        tuple[int, str]: It returns level and tag extracted from the line
    """
    
    line = line.replace('\n','')
    lineList = line.split(' ')

    if 'INDI' in line or ('FAM' in line and 'FAMS' not in line and 'FAMC' not in line):
        tag_index = 2 
    else:
        tag_index = 1
            
    level, tag = lineList[0], lineList[tag_index]
    return level, tag
