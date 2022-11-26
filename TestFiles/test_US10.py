import unittest

from UserStories.us10 import marriage_after_14
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US10"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_marriage_after_14(unittest.TestCase):
    def test_marriage_after_14(self):
        
        for fam_id in families:
            
            husb_id = families[fam_id].get_husband()
            wife_id = families[fam_id].get_wife()
            
            husb_birth_date = individuals[husb_id].get_birth_date()
            wife_birth_date = individuals[wife_id].get_birth_date()
            
            marriage_date = families[fam_id].get_marriage_date()
            
            try:
                self.assertTrue(marriage_after_14(husb_birth_date, wife_birth_date, marriage_date))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)
        