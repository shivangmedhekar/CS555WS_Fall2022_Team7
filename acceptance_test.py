import unittest
from UserStories import *
from Parser.parser import parse
from Classes.Family import Family
from config import GEDCOM_FILE
import datetime

individuals, families = parse(GEDCOM_FILE)
line_length = 125

    
# ---------------------------------------------------------------------------- #
#                        US01: Dates before current date                       #
# ---------------------------------------------------------------------------- #
class Test_US01(unittest.TestCase):
    def test_dates_before_current_date(self):
        
        USER_STORY = "US01"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        try: 
            date = datetime.datetime.strptime('05/24/2010', "%m/%d/%Y").date()
            self.assertTrue(us01.dates_before_current_date(date=date, type='Birthday'))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        try :
            date = datetime.datetime.strptime('05/24/2023', "%m/%d/%Y").date()
            self.assertTrue(us01.dates_before_current_date(date=date, type='Birthday'))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
            
    # ---------------------------------------------------------------------------- #
    #                         US 02: Birth before marriage                         #
    # ---------------------------------------------------------------------------- #
class Test_US02(unittest.TestCase):
    def test_birth_before_marriage(self):
        
        USER_STORY = "US02"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        try: 
            birth_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
            marriage_date = datetime.datetime.strptime('07/10/2022', "%m/%d/%Y").date()
            self.assertTrue(us02.birth_before_marriage(birth_date, marriage_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        try :
            birth_date = datetime.datetime.strptime('05/24/2010', "%m/%d/%Y").date()
            marriage_date = datetime.datetime.strptime('07/10/2009', "%m/%d/%Y").date()
            self.assertTrue(us02.birth_before_marriage(birth_date, marriage_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
            
    # ---------------------------------------------------------------------------- #
    #                           US 03: Birth before death                          #
    # ---------------------------------------------------------------------------- #       
class Test_US03(unittest.TestCase):
    def test_birth_before_death(self):
        
        USER_STORY = "US03"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        try: 
            birth_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
            death_date = datetime.datetime.strptime('07/10/2022', "%m/%d/%Y").date()
            self.assertTrue(us03.birth_before_death(birth_date, death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        try :
            birth_date = datetime.datetime.strptime('05/24/2010', "%m/%d/%Y").date()
            death_date = datetime.datetime.strptime('07/10/2009', "%m/%d/%Y").date()
            self.assertTrue(us03.birth_before_death(birth_date, death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
    
    # ---------------------------------------------------------------------------- #
    #                        US 04: Marriage before divorce                        #
    # ---------------------------------------------------------------------------- #    
class Test_US04(unittest.TestCase):   
    def test_marriage_before_divorce(self):
        
        USER_STORY = "US04"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        try: 
            marriage_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
            divorce_date = datetime.datetime.strptime('07/10/2022', "%m/%d/%Y").date()
            self.assertTrue(us04.marriage_before_divorce(marriage_date, divorce_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        try :
            marriage_date = datetime.datetime.strptime('05/24/2010', "%m/%d/%Y").date()
            divorce_date = datetime.datetime.strptime('07/10/2009', "%m/%d/%Y").date()
            self.assertTrue(us04.marriage_before_divorce(marriage_date, divorce_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
            
    # ---------------------------------------------------------------------------- #
    #                         US 05: Marriage before death                         #
    # ---------------------------------------------------------------------------- # 
class Test_US05(unittest.TestCase):     
    def test_marriage_before_death(self):
        
        USER_STORY = "US05"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        try: 
            marriage_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
            death_date = datetime.datetime.strptime('07/10/2022', "%m/%d/%Y").date()
            self.assertTrue(us05.marriage_before_death(marriage_date, death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        try :
            marriage_date = datetime.datetime.strptime('05/24/2010', "%m/%d/%Y").date()
            death_date = datetime.datetime.strptime('07/10/2009', "%m/%d/%Y").date()
            self.assertTrue(us05.marriage_before_death(marriage_date, death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
    # ---------------------------------------------------------------------------- #
    #                          US 06: Divorce before death                         #
    # ---------------------------------------------------------------------------- #     
class Test_US06(unittest.TestCase):
    def test_divorce_before_death(self):
        
        USER_STORY = "US06"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        try: 
            divorce_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
            death_date = datetime.datetime.strptime('07/10/2022', "%m/%d/%Y").date()
            self.assertTrue(us06.divorce_before_death(divorce_date, death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        try :
            divorce_date = datetime.datetime.strptime('05/24/2010', "%m/%d/%Y").date()
            death_date = datetime.datetime.strptime('07/10/2009', "%m/%d/%Y").date()
            self.assertTrue(us06.divorce_before_death(divorce_date, death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
    # ---------------------------------------------------------------------------- #
    #                        US 07: Less then 150 years old                        #
    # ---------------------------------------------------------------------------- #    
class Test_US07(unittest.TestCase):
    def test_less_then_150_years_old(self):
        
        USER_STORY = "US07"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        try: 
            self.assertTrue(us07.less_then_150_years_old(age = 85))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        try :
            self.assertTrue(us07.less_then_150_years_old(age = 161))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
    # ---------------------------------------------------------------------------- #
    #                    US 08: Birth before marriage of parents                   #
    # ---------------------------------------------------------------------------- # 
class Test_US08(unittest.TestCase):
    def test_birth_before_marriage_of_parents(self):
        
        USER_STORY = "US08"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        child_birth = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
        marriage_of_parents = datetime.datetime.strptime('07/10/1992', "%m/%d/%Y").date()
        divorce_of_parents = datetime.datetime.strptime('07/10/2016', "%m/%d/%Y").date()
        try: 
            self.assertTrue(us08.birth_before_marriage_of_parents(child_birth, marriage_of_parents, divorce_of_parents))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        
        child_birth = datetime.datetime.strptime('05/24/1992', "%m/%d/%Y").date()
        marriage_of_parents = datetime.datetime.strptime('07/10/1992', "%m/%d/%Y").date()
        divorce_of_parents = datetime.datetime.strptime('07/10/2016', "%m/%d/%Y").date()
        
        try :
            self.assertTrue(us08.birth_before_marriage_of_parents(child_birth, marriage_of_parents, divorce_of_parents))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
    # ---------------------------------------------------------------------------- #
    #                     US 09: Birth before death of parents                     #
    # ---------------------------------------------------------------------------- #
class Test_US09(unittest.TestCase):
    def test_child_birth_before_parents_death(self):
        
        USER_STORY = "US09"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        child_birth_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
        father_death_date = datetime.datetime.strptime('07/10/2018', "%m/%d/%Y").date()
        mother_death_date = datetime.datetime.strptime('07/10/2022', "%m/%d/%Y").date()
        try: 
            self.assertTrue(us09.child_birth_before_parents_death(child_birth_date, father_death_date, mother_death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        
        child_birth_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
        father_death_date = datetime.datetime.strptime('07/10/1997', "%m/%d/%Y").date()
        mother_death_date = datetime.datetime.strptime('07/10/2016', "%m/%d/%Y").date()
        
        try :
            self.assertTrue(us09.child_birth_before_parents_death(child_birth_date, father_death_date, mother_death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 2 ------------------------------- #
        
        child_birth_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
        father_death_date = datetime.datetime.strptime('07/10/2016', "%m/%d/%Y").date()
        mother_death_date = datetime.datetime.strptime('07/10/1997', "%m/%d/%Y").date()
        
        try :
            self.assertTrue(us09.child_birth_before_parents_death(child_birth_date, father_death_date, mother_death_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
            
# ---------------------------------------------------------------------------- #
#                           US 10: Marriage after 14                           #
# ---------------------------------------------------------------------------- #
class Test_US10(unittest.TestCase):
    def test_marriage_after_14(self):
        
        USER_STORY = "US10"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        
        husb_birth_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
        wife_birth_date = datetime.datetime.strptime('07/10/1998', "%m/%d/%Y").date()
        marriage_date = datetime.datetime.strptime('07/10/2022', "%m/%d/%Y").date()
        try: 
            self.assertTrue(us10.marriage_after_14(husb_birth_date, wife_birth_date, marriage_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #
        
        husb_birth_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
        wife_birth_date = datetime.datetime.strptime('07/10/1992', "%m/%d/%Y").date()
        marriage_date = datetime.datetime.strptime('07/10/2010', "%m/%d/%Y").date()
        
        try :
            self.assertTrue(us10.marriage_after_14(husb_birth_date, wife_birth_date, marriage_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 2 ------------------------------- #
        
        husb_birth_date = datetime.datetime.strptime('05/24/1992', "%m/%d/%Y").date()
        wife_birth_date = datetime.datetime.strptime('07/10/1997', "%m/%d/%Y").date()
        marriage_date = datetime.datetime.strptime('07/10/2007', "%m/%d/%Y").date()
        
        try :
            self.assertTrue(us10.marriage_after_14(husb_birth_date, wife_birth_date, marriage_date))
            
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
# ---------------------------------------------------------------------------- #
#                               US 11: No Bigamy                               #
# ---------------------------------------------------------------------------- #
class Test_US11(unittest.TestCase):
    def test_no_bigamy(self):
        
        USER_STORY = "US11"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        for ind_id in individuals:
            fams = individuals[ind_id].get_fams_id()
            
            try:
                self.assertTrue(us11.no_bigamy(fams, individuals, families))
            except Exception as e:
                write_errors(user_story = USER_STORY, error = e)
                
        # -------------------------------- Fail Test 1 ------------------------------- #
        I4_death_date = individuals['I4'].get_death_date()
        I7_death_date = individuals['I7'].get_death_date()
        individuals['I4'].set_death_date(None)
        individuals['I7'].set_death_date(None)
        
        for ind_id in individuals:
            fams = individuals[ind_id].get_fams_id()
            try:
                self.assertTrue(us11.no_bigamy(fams, individuals, families))
            except Exception as e:
                write_errors(user_story = USER_STORY, error = e, id = ind_id)
                
        individuals['I4'].set_death_date(I4_death_date)
        individuals['I7'].set_death_date(I7_death_date)
        
# ---------------------------------------------------------------------------- #
#                          US 12: Parents not too old                          #
# ---------------------------------------------------------------------------- #
class Test_US12(unittest.TestCase):
    def test_age_gap_between_child_and_parents(self):
        
        print('⸻' * line_length)
        USER_STORY = "US12"
        
        # -------------------------------- Pass Test 1 ------------------------------- #
        child_birth_date = datetime.datetime.strptime('05/24/1998', "%m/%d/%Y").date()
        father_birth_date = datetime.datetime.strptime('07/10/1967', "%m/%d/%Y").date()
        mother_birth_date = datetime.datetime.strptime('07/10/1955', "%m/%d/%Y").date()
        
        try:
            self.assertTrue(us12.age_gap_between_child_and_parents(child_birth_date, father_birth_date, mother_birth_date))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 1 ------------------------------- #
        child_birth_date = datetime.datetime.strptime('05/24/2022', "%m/%d/%Y").date()
        father_birth_date = datetime.datetime.strptime('07/10/1967', "%m/%d/%Y").date()
        mother_birth_date = datetime.datetime.strptime('07/10/1955', "%m/%d/%Y").date()
        
        try:
            self.assertTrue(us12.age_gap_between_child_and_parents(child_birth_date, father_birth_date, mother_birth_date))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 2 ------------------------------- #
        child_birth_date = datetime.datetime.strptime('05/24/2002', "%m/%d/%Y").date()
        father_birth_date = datetime.datetime.strptime('07/10/1921', "%m/%d/%Y").date()
        mother_birth_date = datetime.datetime.strptime('07/10/1955', "%m/%d/%Y").date()
        
        try:
            self.assertTrue(us12.age_gap_between_child_and_parents(child_birth_date, father_birth_date, mother_birth_date))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        
# ---------------------------------------------------------------------------- #
#                            US 13: Siblings spacing                           #
# ---------------------------------------------------------------------------- # 
class Test_US13(unittest.TestCase):
    def test_siblings_spacing(self):
            
        USER_STORY = "US13"
        print('⸻' * line_length)
            
        # -------------------------------- Pass Test 1 ------------------------------- #  
        birth_dates = ['05/24/1998', '05/24/2000', '05/24/2004', '05/24/2008']
        birth_dates = [datetime.datetime.strptime(date, "%m/%d/%Y").date() for date in birth_dates]
            
        try:
            self.assertTrue(us13.siblings_spacing(birth_dates))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Pass Test 2 ------------------------------- #  
        # Testing dates diffrence for less than 2 days
        birth_dates = ['05/24/1998', '05/26/1998']
        birth_dates = [datetime.datetime.strptime(date, "%m/%d/%Y").date() for date in birth_dates]
            
        try:
            self.assertTrue(us13.siblings_spacing(birth_dates))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 1 ------------------------------- #  
        # Testing dates diffrence for less then 8 months
        birth_dates = ['05/24/1998', '12/24/1998']
        birth_dates = [datetime.datetime.strptime(date, "%m/%d/%Y").date() for date in birth_dates]
            
        try:
            self.assertTrue(us13.siblings_spacing(birth_dates))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
    
# ---------------------------------------------------------------------------- #
#                          US 14: Multiple births <= 5                         #
# ---------------------------------------------------------------------------- #
class Test_US14(unittest.TestCase):
    def test_multiple_births_less_then_equal_to_5(self):
        
        USER_STORY = "US14"
        print('⸻' * line_length)
            
        # -------------------------------- Pass Test 1 ------------------------------- #  
        birth_dates = ['05/24/1998', '05/24/2000', '05/24/2004', '05/24/2008', '05/24/2009', '05/24/2011']
        birth_dates = [datetime.datetime.strptime(date, "%m/%d/%Y").date() for date in birth_dates]
            
        try:
            self.assertTrue(us14.multiple_births_less_then_equal_to_5(birth_dates))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Pass Test 1 ------------------------------- #  
        birth_dates = ['05/24/1998', '05/24/1998', '05/24/1998', '05/24/1998', '05/24/1998']
        birth_dates = [datetime.datetime.strptime(date, "%m/%d/%Y").date() for date in birth_dates]
            
        try:
            self.assertTrue(us14.multiple_births_less_then_equal_to_5(birth_dates))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 1 ------------------------------- #  
        birth_dates = ['05/24/1998', '05/24/1998', '05/24/1998', '05/24/1998', '05/24/1998', '05/24/1998']
        birth_dates = [datetime.datetime.strptime(date, "%m/%d/%Y").date() for date in birth_dates]
            
        try:
            self.assertTrue(us14.multiple_births_less_then_equal_to_5(birth_dates))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
            
# ---------------------------------------------------------------------------- #
#                         US 15: Fewer than 15 siblings                        #
# ---------------------------------------------------------------------------- #
class Test_US15(unittest.TestCase):
    def test_fewer_than_15_siblings(self):
        
        USER_STORY = "US15"
        print('⸻' * line_length)
            
        # -------------------------------- Pass Test 1 ------------------------------- #  
        siblings = ["I" + str(x) for x in range(1, 10)]
        try:
            self.assertTrue(us15.fewer_than_15_siblings(siblings))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 1 ------------------------------- #  
        siblings = ["I" + str(x) for x in range(1, 17)]
        try:
            self.assertTrue(us15.fewer_than_15_siblings(siblings))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            

# ---------------------------------------------------------------------------- #
#                            US 16: Male last names                            #
# ---------------------------------------------------------------------------- #
class Test_US16(unittest.TestCase):
    def test_male_last_names(self):
        
        USER_STORY = "US16"
        print('⸻' * line_length)
            
        # -------------------------------- Pass Test 1 ------------------------------- #  
        family_last_name = 'Stark'
        male_child_names = ['Jack Stark', 'Johnny Stark', 'Eddard Stark', 'John Stark']
        try:
            self.assertTrue(us16.male_last_names(family_last_name, male_child_names))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 1 ------------------------------- #  
        family_last_name = 'Stark'
        male_child_names = ['Jack Stark', 'Johnny Stark', 'Eddard Stark', 'John Targaryen']
        try:
            self.assertTrue(us16.male_last_names(family_last_name, male_child_names))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
            
# ---------------------------------------------------------------------------- #
#                            US 16: Male last names                            #
# ---------------------------------------------------------------------------- #
class Test_US16(unittest.TestCase):
    def test_male_last_names(self):
        
        USER_STORY = "US16"
        print('⸻' * line_length)
            
        # -------------------------------- Pass Test 1 ------------------------------- #  
        family_last_name = 'Stark'
        male_child_names = ['Jack Stark', 'Johnny Stark', 'Eddard Stark', 'John Stark']
        try:
            self.assertTrue(us16.male_last_names(family_last_name, male_child_names))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 1 ------------------------------- #  
        family_last_name = 'Stark'
        male_child_names = ['Jack Stark', 'Johnny Stark', 'Eddard Stark', 'John Targaryen']
        try:
            self.assertTrue(us16.male_last_names(family_last_name, male_child_names))
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            

# ---------------------------------------------------------------------------- #
#                       US 18: Siblings should not marry                       #
# ---------------------------------------------------------------------------- #
class Test_US18(unittest.TestCase):
    def test_no_bigamy(self):
        
        USER_STORY = "US18"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #  
        for fam_id in families:
            children = families[fam_id].get_children()
            
            try:
                self.assertTrue(us18.siblings_should_not_marry(siblings=children,
                                                          individuals=individuals, famalies=families))      
            
            except Exception as e:
                write_errors(user_story = USER_STORY, error = e)
                
        # -------------------------------- Fail Test 1 ------------------------------- # 
        
        individuals['I5'].set_fams_id(['F6']) 
        individuals['I6'].set_fams_id(['F3', 'F6'])
        families['F6'] = Family(famID='F6', husband = 'I5', wife = 'I6', marriage_date = None, divorce_date = None, children = [])
        
        for fam_id in families:
            children = families[fam_id].get_children()
            try:
                self.assertTrue(us18.siblings_should_not_marry(siblings=children,
                                                          individuals=individuals, famalies=families))      
            
            except Exception as e:
                write_errors(user_story = USER_STORY, error = e)
                
        individuals['I5'].set_fams_id([]) 
        individuals['I6'].set_fams_id(['F3'])
        del families['F6']
        
# ---------------------------------------------------------------------------- #
#                            US 20: Aunts and uncles                           #
# ---------------------------------------------------------------------------- #
class Test_US20(unittest.TestCase):
    def test_aunts_and_uncles(self):
        
        USER_STORY = "US20"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #  
        for fam_id in families:
            try:
                self.assertTrue(us20.aunts_and_uncles(family = fam_id, individuals=individuals, famalies=families))   
                
            except Exception as e:
                write_errors(user_story = USER_STORY, error = e)
                
         # -------------------------------- Fail Test 1 ------------------------------- # 
        individuals['I5'].set_fams_id(['F6']) 
        individuals['I10'].set_fams_id(['F6'])
        families['F6'] = Family(famID='F6', husband = 'I5', wife = 'I10', marriage_date = None, divorce_date = None, children = [])
        for fam_id in families:
            try:
                self.assertTrue(us20.aunts_and_uncles(family = fam_id, individuals=individuals, famalies=families))   
                
            except Exception as e:
                write_errors(user_story = USER_STORY, error = e)
        
        individuals['I5'].set_fams_id([]) 
        individuals['I10'].set_fams_id([])
        del families['F6']
        
# ---------------------------------------------------------------------------- #
#                        US 21: Correct gender for role                        #
# ---------------------------------------------------------------------------- #
class Test_US21(unittest.TestCase):
    def test_correct_gender_for_role(self):
        
        USER_STORY = "US21"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #  
        for fam_id in families:
            try:
                self.assertTrue(us21.correct_gender_for_role(fam_id, individuals, families))   
                
            except Exception as e:
                write_errors(user_story = USER_STORY, error = e)
                
         # -------------------------------- Fail Test 1 ------------------------------- # 
        individuals['I2'].set_gender('M')
        for fam_id in families:
            try:
                self.assertTrue(us21.correct_gender_for_role(fam_id, individuals, families))   
                
            except Exception as e:
                write_errors(user_story = USER_STORY, error = e)
                
        individuals['I2'].set_gender('F')
        
# ---------------------------------------------------------------------------- #
#                               US 22: Unique IDs                              #
# ---------------------------------------------------------------------------- #
class Test_US22(unittest.TestCase):
    def test_unique_IDs(self):
        
        USER_STORY = "US22"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #  
        
        indIDs = [ind_id for ind_id in individuals]
        famIDs = [fam_id for fam_id in families]

        try:
            self.assertTrue(us22.unique_IDs(indIDs, famIDs))
           
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        # -------------------------------- Fail Test 1 ------------------------------- #  
        
        indIDs = [ind_id for ind_id in individuals]
        famIDs = [fam_id for fam_id in families]
        
        indIDs[1] = 'I1'

        try:
            self.assertTrue(us22.unique_IDs(indIDs, famIDs))
           
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
# ---------------------------------------------------------------------------- #
#                       US 23: Unique name and birth date                      #
# ---------------------------------------------------------------------------- #
class Test_US23(unittest.TestCase):
    def test_unique_name_and_birthdate(self):
        
        USER_STORY = "US23"
        print('⸻' * line_length)
        
        # -------------------------------- Pass Test 1 ------------------------------- #  
        
        indIDs = [ind_id for ind_id in individuals]

        try:
            self.assertTrue(us23.unique_name_and_birthdate(indIDs, individuals))
           
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
            
        # -------------------------------- Fail Test 1 ------------------------------- #  
        
        indIDs = [ind_id for ind_id in individuals]
        individuals['I2'].set_name('Richard Stark')
        individuals['I2'].set_birth_date(datetime.datetime.strptime('04/08/1936', "%m/%d/%Y").date())

        try:
            self.assertTrue(us23.unique_name_and_birthdate(indIDs, individuals))
           
        except Exception as e:
            write_errors(user_story = USER_STORY, error = e)
        
        individuals['I2'].set_name('Layarra Targaryen')
        individuals['I2'].set_birth_date(datetime.datetime.strptime('07/08/1940', "%m/%d/%Y").date())
        
            
        
            
        
        
        
        
        
        
        

def write_errors(user_story, error, id=''):
    
    error_msg = create_error_msg(user_story, error, id)
    print(error_msg)
    # with open("output.txt", "a") as output_file:
    #     print(error_msg)
    #     output_file.write(error_msg)
    #     output_file.write("\n")
        
def create_error_msg(user_story, error, id='') -> str:
    if len(id):
        return f'ERROR: {user_story}: {id}: {error}'   
    else:
        return f'ERROR: {user_story}: {error}'      

if __name__ == '__main__':
    unittest.main()

