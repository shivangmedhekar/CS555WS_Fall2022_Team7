from math import fabs
import unittest

from UserStories.us16 import male_last_names
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us16"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_male_last_names(unittest.TestCase):
    def test_male_last_names(self):
        
        for fam_id in families:
            try:
                self.assertTrue(male_last_names(fam_id, individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)