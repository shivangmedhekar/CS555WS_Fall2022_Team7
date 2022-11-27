import unittest

from UserStories.us05 import marriage_before_death
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US05"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_marriage_before_death(unittest.TestCase):
    def test_marriage_before_death(self):
        
        for ind_id in individuals:

            death = individuals[ind_id].get_death_date()

            fams = individuals[ind_id].get_fams_id()
            for fam in fams:
                marriage = families[fam].get_marriage_date()

                try:
                    self.assertTrue(marriage_before_death(marriage, death))
                except Exception as e:
                    write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)