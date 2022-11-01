import unittest
from Classes.Family import Family

from UserStories.us18 import siblings_should_not_marry
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US18"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_siblings_should_not_marry(unittest.TestCase):
    def test_siblings_should_not_marry(self):
        
        for fam_id in families:
            children = families[fam_id].get_children()
            
            try:
                self.assertTrue(siblings_should_not_marry(siblings=children,
                                                          individuals=individuals, famalies=families))      
            
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)