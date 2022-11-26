from math import fabs
import unittest

from UserStories.us16 import male_last_names
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us16"
type = "FAMILY"

individuals, families = parse(GEDCOM_FILE)

class Test_male_last_names(unittest.TestCase):
    def test_male_last_names(self):
        
        for fam_id in families:
            
            husb_id = families[fam_id].get_husband()
            husb_name = individuals[husb_id].get_name()
            
            family_last_name = husb_name.split()[1]
            
            children = families[fam_id].get_children()
            
            male_children = [child_id for child_id in children if individuals[child_id].get_gender() == 'M']
            male_child_names = [individuals[child_id].get_name() for child_id in male_children]
            
            try:
                self.assertTrue(male_last_names(family_last_name, male_child_names))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = fam_id, error = e)