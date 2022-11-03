from math import fabs
import unittest

from UserStories.us35 import list_recent_births
from Parser.parser import parse
from write_errors import write_errors

from config import GEDCOM_FILE

USER_STORY = "us35"
type = "INDIVIDUAL"

individuals, families = parse(GEDCOM_FILE)

class Test_list_recent_birth(unittest.TestCase):
    def test_list_recent_birth(self):

        self.assertIsInstance(list_recent_births(individuals), dict)