from datetime import datetime
from dateutil.relativedelta import relativedelta
from Classes.Individual import Individual
from Classes.Family import Family

VALID_TAGS = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR',
            'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


def parse(GEDCOM_FILE):

    individuals, families = {}, {}

    with open(GEDCOM_FILE, 'r') as file:

        lines = file.readlines()
        i = 0

        while(i < len(lines)):

            level, tag = get_level_n_tag(lines[i])

            if "INDI" in lines[i]:
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
                    
                    if ("FAMC" == tag and level == "1"):
                        famcID.append(lines[i].split("@")[1])

                    elif ("FAMS" == tag and level == "1"):
                        famsID.append(lines[i].split("@")[1])
                    
                    elif ("NAME" == tag and level == "1"):
                        name = lines[i][7:len(lines[i]) - 1].replace("/", "").replace("\n", "")
                    
                    elif ("SEX" == tag and level == "1"):
                        sex = lines[i][6]

                    elif ("BIRT" == tag and level == "1"):
                        i = i + 1
                        birth = parse_date(lines[i].replace("2 DATE ", ''))

                    elif ("DEAT" == tag and level == "1"):
                        i = i + 1
                        death = parse_date(lines[i].replace("2 DATE ", ''))

                    if ("TRLR" == tag or "FAM" == tag):
                        break

                    i = i + 1
                
                individuals[indID] = (Individual(indID, famcID, famsID, name, sex, birth, death))

            elif ("FAM" in lines[i] and "FAMC" not in lines[i] and "FAMS" not in lines[i]):
                famID = lines[i].split("@")[1]
                husband = None
                wife = None
                marriageDate = None
                divorceDate = None
                children = []
                i = i + 1
                while (True):
                    
                    if ("1 HUSB" in lines[i]):
                        husband = lines[i].split("@")[1]
                    #Parse out the wife
                    elif ("1 WIFE" in lines[i]):
                        wife = lines[i].split("@")[1]
                    #Parse out the marriage date
                    elif ("1 MARR" in lines[i]):
                        i = i + 1
                        marriageDate = parse_date(lines[i].replace("2 DATE ", ''))
                    elif ("DIV" in lines[i]):
                        i = i + 1
                        divorceDate = parse_date(lines[i].replace("2 DATE ", ''))
                    #Parse out the children
                    elif ("1 CHIL" in lines[i]):
                        children.append(lines[i].split("@")[1])

                    elif ("0 TRLR" in lines[i]) or ("FAM" in lines[i] and "FAMC" not in lines[i] and "FAMS" not in lines[i]):
                        break

                    if ("0 TRLR" in lines[i]):
                        break
                    i = i + 1
                families[famID] = (Family(famID, husband, wife, marriageDate, divorceDate, children))

            if "0 TRLR" in lines[i]:
                break

            if "INDI" not in lines[i] and tag != "FAM":
                i = i + 1
    
    return individuals, families

# Helper Functions

def parse_date(date):

    try: 
        day, month, year = date.split(" ")
        month = MONTHS.index(month.upper()) + 1
        day, month, year = int(day), int(month), int(year)

        datetime_element = datetime(year, month, day)
        
        age = datetime.now() - datetime_element
        #print(age)
        date_1 = datetime(2022, 12, 2)
        #print((datetime.now() - date_1).days)
        difference_in_years = relativedelta(datetime.now(), datetime_element)
        #print(difference_in_years.days)
        return datetime_element.date()
    except:
        print(date)
        return None


def get_level_n_tag(line):
    
    line = line.replace('\n','')
    lineList = line.split(' ')

    if 'INDI' in line or ('FAM' in line and 'FAMS' not in line and 'FAMC' not in line):
        tag_index = 2 
    else:
        tag_index = 1
            
    level, tag = lineList[0], lineList[tag_index]
    return level, tag
