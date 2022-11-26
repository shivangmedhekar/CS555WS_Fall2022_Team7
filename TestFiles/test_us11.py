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
    def test_no_bigamy(self):
        
        for ind_id in individuals:
            try:
                self.assertTrue(no_bigamy(individuals[ind_id].get_fams_id(), individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)