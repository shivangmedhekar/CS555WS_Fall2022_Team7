import unittest

from UserStories.us01 import dates_before_current_date
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = 'US01'
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_dates_before_current_date(unittest.TestCase):
    
    def test_dates_before_current_date(self):
        
        for ind_id in individuals:

            birth = individuals[ind_id].get_birth_date()
            death = individuals[ind_id].get_death_date()

            try:
                self.assertTrue(dates_before_current_date(date = birth, type = "Birthday"))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)
            
            try:
                self.assertTrue(dates_before_current_date(date = death, type = "Deathday"))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)


            fams = individuals[ind_id].get_fams_id()
            for fam in fams:

                marriage = families[fam].get_marriage_date()
                divorce = families[fam].get_divorce_date()

                try:
                    self.assertTrue(dates_before_current_date(date=marriage, type="Marriage"))
                except Exception as e:
                    write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)

                try:
                    self.assertTrue(dates_before_current_date(date=divorce, type="Divorce"))
                except Exception as e:
                    write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)