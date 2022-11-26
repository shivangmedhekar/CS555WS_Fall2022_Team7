import unittest
from UserStories import *
import datetime

class Test_all_user_stories(unittest.TestCase):
    
    # ---------------------------------------------------------------------------- #
    #                        US01: Dates before current date                       #
    # ---------------------------------------------------------------------------- #
    def test_dates_before_current_date(self):
        
        USER_STORY = "US01"
        
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
    def test_birth_before_marriage(self):
        
        USER_STORY = "US02"
        
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
    def test_birth_before_death(self):
        
        USER_STORY = "US03"
        
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
    def test_marriage_before_divorce(self):
        
        USER_STORY = "US04"
        
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
    def test_marriage_before_death(self):
        
        USER_STORY = "US05"
        
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
    def test_divorce_before_death(self):
        
        USER_STORY = "US06"
        
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
    def test_less_then_150_years_old(self):
        
        USER_STORY = "US07"
        
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
    def test_birth_before_marriage_of_parents(self):
        
        USER_STORY = "US08"
        
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
    def test_child_birth_before_parents_death(self):
        
        USER_STORY = "US09"
        
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
            



    



def write_errors(user_story, error):
    
    error_msg = create_error_msg(user_story, error)
    print(error_msg)
    # with open("output.txt", "a") as output_file:
    #     print(error_msg)
    #     output_file.write(error_msg)
    #     output_file.write("\n")
        
def create_error_msg(user_story, error) -> str:
    return f'ERROR: {user_story}: {error}'        

if __name__ == '__main__':
    unittest.main()

