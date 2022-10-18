import unittest
from UserStories.user_stories import *
import sys, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Parser.parser import parse

GEDCOM_FILE = 'GEDCOM_FILES/Stark_Family.ged'

individuals, families = parse(GEDCOM_FILE)

class Test_user_stories(unittest.TestCase):

    
    def test_dates_before_current_date(self):
        
        for indID in individuals:

            birth = individuals[indID].get_birthday()
            death = individuals[indID].get_deathday()

            self.assertTrue(dates_before_current_date(birth, type="Birthday"))
            self.assertTrue(dates_before_current_date(death, type="Deathday"))

            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                divorce = families[fam].get_divorce_date()
                self.assertTrue(dates_before_current_date(marriage, type="Marriage"))
                self.assertTrue(dates_before_current_date(divorce, type="Divorce"))

    def test_birth_before_marriage(self):
        
        for indID in individuals:

            birth = individuals[indID].get_birthday()
            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                self.assertTrue(birth_before_marriage(birth, marriage))

    def test_birth_before_death(self):
        
        for indID in individuals:

            birth = individuals[indID].get_birthday()
            death = individuals[indID].get_deathday()
            self.assertTrue(birth_before_death(birth, death))

    def test_marriage_before_divorce(self):

        for indID in individuals:
        
            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                divorce = families[fam].get_divorce_date()
                self.assertTrue(marriage_before_divorce(marriage, divorce))

    def test_marriage_before_death(self):
        
        for indID in individuals:
            death = individuals[indID].get_deathday()

            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                self.assertTrue(marriage_before_death(marriage, death))

    def test_divorce_before_death(self):
        
        for indID in individuals:
            death = individuals[indID].get_deathday()
            fams = individuals[indID].get_famsID()
            for fam in fams:
                divorce = families[fam].get_divorce_date()
                self.assertTrue(divorce_before_death(divorce, death))

    def test_less_then_150_years_old(self):
        
        for indID in individuals:
            age = individuals[indID].get_age().years
            self.assertTrue(less_then_150_years_old(age))

if __name__ == '__main__':
    unittest.main()