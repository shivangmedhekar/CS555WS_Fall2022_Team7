from math import fabs
import unittest

from UserStories.us08 import birth_before_marriage_of_parents
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US08"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_birth_before_marriage_of_parents(unittest.TestCase):
    def test_birth_before_marriage_of_parents(self):

        for fam_id in families:
            
            children = families[fam_id].get_children()
            marriage_of_parents = families[fam_id].get_marriage_date()
            divorce_of_parents = families[fam_id].get_divorce_date()
            
            if children:
                for child in children:
                    child_birth = individuals[child].get_birth_date()
                    try:
                        self.assertTrue(birth_before_marriage_of_parents(child_birth, marriage_of_parents, divorce_of_parents))
                    except Exception as e:
                        write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)
