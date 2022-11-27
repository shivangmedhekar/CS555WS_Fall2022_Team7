import unittest

from UserStories.us21 import correct_gender_for_role
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US21"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_correct_gender_for_role(unittest.TestCase):
    def test_correct_gender_for_role(self):
        
        for fam_id in families:
            try:
                self.assertTrue(correct_gender_for_role(fam_id, individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = 'fam_id', error = e)

        