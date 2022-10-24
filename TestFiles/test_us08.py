from math import fabs
import unittest

from UserStories.us08 import no_children_without_marriage
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US08"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_no_children_without_marriage(unittest.TestCase):
    def test_less_then_150_years_old(self):
        
        for ind_id in individuals:
            try:
                self.assertTrue(no_children_without_marriage(individuals[ind_id].get_fams_id(), individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)
