from math import fabs
import unittest

from UserStories.us09 import child_birth_before_parents_death
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US09"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_child_birth_before_parents_death(unittest.TestCase):
    def test_child_birth_before_parents_death(self):
        
        for fam_id in families:
            
            children = families[fam_id].get_children()
            
            husb_id = families[fam_id].get_husband()
            wife_id = families[fam_id].get_wife()
            
            husb_death_date = individuals[husb_id].get_death_date()
            wife_death_date = individuals[wife_id].get_death_date()
            
            
            if children:
                for child in children:
                    child_birth = individuals[child].get_birth_date()
                    try:
                        self.assertTrue(child_birth_before_parents_death(child_birth_date = child_birth, father_death_date = husb_death_date, mother_death_date = wife_death_date))
                    except Exception as e:
                        write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)
        
