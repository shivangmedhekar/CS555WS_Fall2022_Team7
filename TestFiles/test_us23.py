import unittest

from UserStories.us23 import unique_name_and_birthdate
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US23"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_unique_name_and_birthdate(unittest.TestCase):
    def test_unique_name_and_birthdate(self):

        ind_ids = list(individuals.keys())

        try:
            self.assertTrue(unique_name_and_birthdate(ind_ids, individuals))
        except Exception as e:
            write_errors(type = type, user_story = USER_STORY, id = 'ind_id', error = e)