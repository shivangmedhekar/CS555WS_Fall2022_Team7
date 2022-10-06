import unittest

from UserStories.us03 import birth_before_death
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

individuals, families = parse(GEDCOM_FILE)
error_message = "ERROR: INDIVIDUAL: US03: {}: {}"

class Test_test_birth_before_death(unittest.TestCase):
    def test_birth_before_death(self):
        
        for indID in individuals:

            birth = individuals[indID].get_birthday()
            death = individuals[indID].get_deathday()

            try:
                self.assertTrue(birth_before_death(birth, death))
            except Exception as e:
                write_errors(error_message.format(indID, e))