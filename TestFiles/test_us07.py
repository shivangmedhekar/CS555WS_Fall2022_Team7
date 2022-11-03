import unittest

from UserStories.us07 import less_then_150_years_old
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US07"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_less_then_150_years_old(unittest.TestCase):
    def test_less_then_150_years_old(self):
        
        for ind_id in individuals:

            age = individuals[ind_id].get_age().years
            try:
                self.assertTrue(less_then_150_years_old(age))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)

                