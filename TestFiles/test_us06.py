import unittest

from UserStories.us06 import divorce_before_death
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US06"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_divorce_before_death(unittest.TestCase):
    def test_divorce_before_death(self):
        
        for ind_id in individuals:

            death = individuals[ind_id].get_death_date()
            fams = individuals[ind_id].get_fams_id()

            for fam in fams:
                divorce = families[fam].get_divorce_date()

                try:
                    self.assertTrue(divorce_before_death(divorce, death))
                except Exception as e:
                    write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)