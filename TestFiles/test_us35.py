from math import fabs
import unittest

from UserStories.us35 import recent_birth
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us35"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_recent_birth(unittest.TestCase):
    def test_recent_birth(self):

        self.assertIsInstance(recent_birth(individuals),list)