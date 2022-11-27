import unittest

from UserStories.us14 import multiple_births_less_then_equal_to_5
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US14"
type = "FAMILY" 

individuals, families = parse(GEDCOM_FILE)

class Test_multiple_births_less_then_equal_to_5(unittest.TestCase):
    def test_multiple_births_less_then_equal_to_5(self):
        
        for fam_id in families:
            
            children = families[fam_id].get_children()
            if len(children):
                children_birth_dates = [individuals[child].get_birth_date() for child in children]
                try:
                    self.assertTrue(multiple_births_less_then_equal_to_5(children_birth_dates))
                except Exception as e:
                    write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)