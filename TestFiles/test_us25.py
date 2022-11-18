import unittest
from Classes.Family import Family

from UserStories.us25 import unique_first_names_in_families
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US25"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_siblings_should_not_marry(unittest.TestCase):
    def test_siblings_should_not_marry(self):
        
        for fam_id in families:
            children = families[fam_id].get_children()
            try:
                self.assertTrue(unique_first_names_in_families(children = children, individuals=individuals))   
                
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = "fam_id", error = e)