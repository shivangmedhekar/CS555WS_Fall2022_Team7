from math import fabs
import unittest

from UserStories.us10 import marriage_after_14
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US10"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_marriage_after_14(unittest.TestCase):
    def test_less_then_150_years_old(self):
        
        for indID in individuals:
            try:
                self.assertTrue(marriage_after_14(individuals[indID].get_famsID(), individuals, families))
            except Exception as e:
                print("ERROR: INDIVIDUAL: US10: {}: {}".format(indID, e))