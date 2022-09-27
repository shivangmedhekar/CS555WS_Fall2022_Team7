
GEDCOM_FILE = 'Stark_Family_Shivang_Medhekar.ged'

with open(GEDCOM_FILE, 'r') as file, open('output.txt', 'w') as output:

    lines = file.readlines()
    
    tags = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR',
            'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

    for line in lines:
        line = line.replace('\n','')
        lineList = line.split(' ')

        if 'INDI' in line or ('FAM' in line and 'FAMS' not in line and 'FAMC' not in line):
            tag_index = 2 
        else:
            tag_index = 1

        level, tag = lineList[0], lineList[tag_index]
        
        valid = 'N'
        if tag in tags:
            valid = 'Y'

        lineList.pop(tag_index)
        lineList.pop(0)

        arguments = " ".join(lineList)

        print("--> {}".format(line))
        output.write("--> {}\n".format(line))
        print("<-- {}|{}|{}|{}".format(level, tag, valid, arguments))
        output.write("<-- {}|{}|{}|{}\n".format(level, tag, valid, arguments))