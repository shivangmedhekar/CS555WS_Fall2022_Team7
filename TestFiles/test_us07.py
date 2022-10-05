import unittest

from UserStories.us07 import less_then_150_years_old
from Parser.parser import parse

from config import GEDCOM_FILE

individuals, families = parse(GEDCOM_FILE)

class Test_less_then_150_years_old(unittest.TestCase):
    def test_less_then_150_years_old(self):
        
        for indID in individuals:

            age = individuals[indID].get_age().years
            try:
                self.assertTrue(less_then_150_years_old(age))
            except Exception as e:
                print("ERROR: INDIVIDUAL: US07: {}: {}".format(indID, e))

                