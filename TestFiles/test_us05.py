import unittest

from UserStories.us05 import marriage_before_death
from Parser.parser import parse

from config import GEDCOM_FILE

individuals, families = parse(GEDCOM_FILE)

class Test_marriage_before_death(unittest.TestCase):
    def test_marriage_before_death(self):
        
        for indID in individuals:

            death = individuals[indID].get_deathday()

            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()

                try:
                    self.assertTrue(marriage_before_death(marriage, death))
                except Exception as e:
                    print("ERROR: INDIVIDUAL: US05: {}: {}".format(indID, e))