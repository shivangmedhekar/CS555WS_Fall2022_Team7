from math import fabs
import unittest

from UserStories.us11 import no_bigamy
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US11"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_no_bigamy(unittest.TestCase):
    def test_less_then_150_years_old(self):
        
        for indID in individuals:
            try:
                self.assertTrue(no_bigamy(individuals[indID].get_fams_id(), individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = indID, error = e)