import unittest

from UserStories.us05 import marriage_before_death
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US05"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_marriage_before_death(unittest.TestCase):
    def test_marriage_before_death(self):
        
        for indID in individuals:

            death = individuals[indID].get_death_date()

            fams = individuals[indID].get_fams_id()
            for fam in fams:
                marriage = families[fam].get_marriage_date()

                try:
                    self.assertTrue(marriage_before_death(marriage, death))
                except Exception as e:
                    write_errors(type = type, user_story = USER_STORY, id = indID, error = e)