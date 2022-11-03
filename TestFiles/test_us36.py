from math import fabs
import unittest

from UserStories.us36 import recent_death
from Parser.parser import parse
from write_errors import write_errors 

from config import GEDCOM_FILE

USER_STORY = "us36"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_recent_death(unittest.TestCase):
    def test_recent_death(self):

        self.assertIsInstance(recent_death(individuals),dict)