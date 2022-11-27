import unittest
from Classes.Family import Family

from UserStories.us15 import fewer_than_15_siblings
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US18"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_fewer_than_15_siblings(unittest.TestCase):
    def test_fewer_than_15_siblings(self):
        
        for fam_id in families:
            children = families[fam_id].get_children()
            
            try:
                self.assertTrue(fewer_than_15_siblings(siblings=children))
            
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)