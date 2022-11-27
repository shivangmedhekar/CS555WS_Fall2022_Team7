import unittest

from UserStories.us22 import unique_IDs
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US22"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_unique_IDs(unittest.TestCase):
    def test_unique_IDs(self):

        ind_ids = list(individuals.keys())
        fam_ids = list(families.keys())
        
        try:
            self.assertTrue(unique_IDs(ind_ids, fam_ids))
        except Exception as e:
            write_errors(type = type, user_story = USER_STORY, id = 'ind_id', error = e)