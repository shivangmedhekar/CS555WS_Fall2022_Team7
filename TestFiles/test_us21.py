from math import fabs
import unittest

from UserStories.us21 import correct_gender_for_role
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us21"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_correct_gender_for_role(unittest.TestCase):
    def test_correct_gender_for_role(self):


        famIDs = []
        
        for fam_id in families:
            famIDs.append(fam_id)

        try:
            self.assertTrue(correct_gender_for_role(famIDs,families, individuals))
        except Exception as e:
            write_errors(type = type, user_story = USER_STORY, id = 'fam_id', error = e)