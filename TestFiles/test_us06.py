import unittest

from UserStories.us06 import divorce_before_death
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US06"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_divorce_before_death(unittest.TestCase):
    def test_divorce_before_death(self):
        
        for indID in individuals:

            death = individuals[indID].get_deathday()
            fams = individuals[indID].get_famsID()

            for fam in fams:
                divorce = families[fam].get_divorce_date()

                try:
                    self.assertTrue(divorce_before_death(divorce, death))
                except Exception as e:
                    print("ERROR: INDIVIDUAL: US06: {}: {}".format(indID, e))