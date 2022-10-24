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
        
        for ind_id in individuals:
            try:
                fam_id = individuals[ind_id].get_famc_id()
                
                if len(fam_id):
                    siblings = families[fam_id[0]].get_children()
                    self.assertTrue(siblings_spacing(siblings, individuals))
                    
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)