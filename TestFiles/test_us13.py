from math import fabs
import unittest

from UserStories.us13 import siblings_spacing
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US13"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_siblings_spacing(unittest.TestCase):
    def test_siblings_spacing(self):
        
        for indID in individuals:
            try:
                famID = individuals[indID].get_famc_id()
                
                if len(famID):
                    siblings = families[famID[0]].get_children()
                    self.assertTrue(siblings_spacing(siblings, individuals))
                    
            except Exception as e:
                print("ERROR: INDIVIDUAL: US013: {}: {}".format(indID, e))