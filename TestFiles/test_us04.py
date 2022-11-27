import unittest

from UserStories.us04 import marriage_before_divorce
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US04"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_marriage_before_divorce(unittest.TestCase):
    def test_marriage_before_divorce(self):
        
        for ind_id in individuals:

            fams = individuals[ind_id].get_fams_id()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                divorce = families[fam].get_divorce_date()

                try:
                    self.assertTrue(marriage_before_divorce(marriage, divorce))
                except Exception as e:
                    write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)