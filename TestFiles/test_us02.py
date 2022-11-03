import unittest

from UserStories.us02 import birth_before_marriage
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US02"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_test_birth_before_marriage(unittest.TestCase):

    def test_birth_before_marriage(self):
        
        for ind_id in individuals:

            birth = individuals[ind_id].get_birth_date()
            fams = individuals[ind_id].get_fams_id()
            
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                
                try:
                    self.assertTrue(birth_before_marriage(birth, marriage))
                except Exception as e:
                    print("ERROR: INDIVIDUAL: US02: {}: {}".format(ind_id, e))