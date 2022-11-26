import unittest

from UserStories.us13 import siblings_spacing
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US13"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_siblings_spacing(unittest.TestCase):
    def test_siblings_spacing(self):
        
        for fam_id in families:
            
            children = families[fam_id].get_children()
            birth_dates = [individuals[child_id].get_birth_date() for child_id in children]
            
            try:
                self.assertTrue(siblings_spacing(birth_dates))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)