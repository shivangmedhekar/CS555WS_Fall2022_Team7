from math import fabs
import unittest

from UserStories.us09 import child_birth_before_parents_death
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US09"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_child_birth_before_parents_death(unittest.TestCase):
    def test_child_birth_before_parents_death(self):
        
        for indID in individuals:
            try:
                self.assertTrue(child_birth_before_parents_death(individuals[indID].get_famsID(), individuals, families))
            except Exception as e:
                print("ERROR: INDIVIDUAL: US09: {}: {}".format(indID, e))
