from math import fabs
import unittest

from UserStories.us16 import all_males_have_same_last_name
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us16"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_all_males_have_same_last_name(unittest.TestCase):
    def test_all_males_have_same_last_name(self):
        
        for indID in individuals:
            try:
                self.assertTrue(all_males_have_same_last_name(individuals[indID].get_fams_id(), individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = indID, error = e)