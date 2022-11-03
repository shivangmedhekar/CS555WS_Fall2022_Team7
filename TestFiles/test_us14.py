import unittest

from UserStories.us14 import multiple_births_less_then_equal_to_5
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US14"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_multiple_births_less_then_equal_to_5(unittest.TestCase):
    def test_multiple_births_less_then_equal_to_5(self):
        
        for ind_id in individuals:
            try:
                self.assertTrue(multiple_births_less_then_equal_to_5(fams_id_list = individuals[ind_id].get_fams_id(),
                                                                     individuals = individuals, 
                                                                     families = families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)