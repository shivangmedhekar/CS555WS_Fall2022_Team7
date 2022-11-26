from math import fabs
import unittest

from UserStories.us23 import unique_name_and_birthdate
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us23"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_unique_name_and_birthdate(unittest.TestCase):
    def test_unique_name_and_birthdate(self):

        indIDs = []
        
        for ind_id in individuals:
            indIDs.append(ind_id)

        try:
            self.assertTrue(unique_name_and_birthdate(indIDs, individuals))
        except Exception as e:
            write_errors(type = type, user_story = USER_STORY, id = 'ind_id', error = e)