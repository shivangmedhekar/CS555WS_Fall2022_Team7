from math import fabs
import unittest

from UserStories.us12 import age_gap_between_child_and_parents
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US12"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_age_gap_between_child_and_parents(unittest.TestCase):
    def test_age_gap_between_child_and_parents(self):
        
        for fam_id in families:

            husb_id = families[fam_id].get_husband()
            wife_id = families[fam_id].get_wife()
            
            husb_birth_date = individuals[husb_id].get_birth_date()
            wife_birth_date = individuals[wife_id].get_birth_date()
            
            children = families[fam_id].get_children()
            for child_id in children:
                child_birth_date = individuals[child_id].get_birth_date()
                try:
                    self.assertTrue(age_gap_between_child_and_parents(child_birth_date = child_birth_date, father_birth_date = husb_birth_date, mother_birth_date = wife_birth_date))
                except Exception as e:
                    write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)
        