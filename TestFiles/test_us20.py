import unittest
from Classes.Family import Family

from UserStories.us20 import aunts_and_uncles
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US20"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_siblings_should_not_marry(unittest.TestCase):
    def test_siblings_should_not_marry(self):
        
        for fam_id in families:
        
            try:
                self.assertTrue(aunts_and_uncles(fam_id = fam_id, individuals=individuals, famalies=families))   
                
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = "fam_id", error = e)