from math import fabs
import unittest

from UserStories.us11 import no_bigamy
from ProjectUtils.parser import parse
from write_errors import write_errors

from ProjectUtils.config import GEDCOM_FILE

USER_STORY = "US11"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_no_bigamy(unittest.TestCase):
    def test_no_bigamy(self):
        
        for ind_id in individuals:
            fams = individuals[ind_id].get_fams_id()
            
            try:
                self.assertTrue(no_bigamy(fams, individuals, families))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = ind_id, error = e)