import unittest

from UserStories.us10 import marriage_after_14
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US10"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_marriage_after_14(unittest.TestCase):
    def test_marriage_after_14(self):
        
        for ind_id in individuals:
            try:
                self.assertTrue(marriage_after_14(individuals[ind_id].get_fams_id(), individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)