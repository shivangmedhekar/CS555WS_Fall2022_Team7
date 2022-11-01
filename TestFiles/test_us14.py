from math import fabs
import unittest

from UserStories.us14 import multiple_babies_more_than_5
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us14"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_multiple_babies_more_than_5(unittest.TestCase):
    def test_multiple_babies_more_than_5(self):
        
        for indID in individuals:
            try:
                self.assertTrue(multiple_babies_more_than_5(individuals[indID].get_fams_id(), individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = indID, error = e)