import unittest

from UserStories.us03 import birth_before_death
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "US03"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_test_birth_before_death(unittest.TestCase):
    def test_birth_before_death(self):
        
        for indID in individuals:

            birth = individuals[indID].get_birthday()
            death = individuals[indID].get_deathday()

            try:
                self.assertTrue(birth_before_death(birth, death))
            except Exception as e:
                write_errors(type = type, user_story = USER_STORY, id = indID, error = e)