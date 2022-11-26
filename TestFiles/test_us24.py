from math import fabs
import unittest

from UserStories.us24 import unique_families_by_spouces
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us24"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_unique_families_by_spouces(unittest.TestCase):
    def test_unique_families_by_spouces(self):

        famIDs = []
        
        for fam_id in families:
            famIDs.append(fam_id)

        try:
            self.assertTrue(unique_families_by_spouces(famIDs, families))
        except Exception as e:
            write_errors(type = type, user_story = USER_STORY, id = 'fam_id', error = e)