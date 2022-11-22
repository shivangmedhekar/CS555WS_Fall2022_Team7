from math import fabs
import unittest

from UserStories.us22 import unique_IDs
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us22"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_unique_IDs(unittest.TestCase):
    def test_unique_IDs(self):

        indIDs = []
        
        for ind_id in individuals:
            indIDs.append(ind_id)

        famIDs = []
        
        for fam_id in families:
            famIDs.append(fam_id)

        try:
            self.assertTrue(unique_IDs(indIDs, famIDs))
        except Exception as e:
            write_errors(type = type, user_story = USER_STORY, id = 'ind_id', error = e)