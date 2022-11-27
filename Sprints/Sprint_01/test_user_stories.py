import unittest
from user_stories import *
import sys, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from ProjectUtils.parser import parse

GEDCOM_FILE = 'GEDCOM_FILES/Stark_Family.ged'

class test_user_stories(unittest.TestCase):

    
    def test_dates_before_current_date(self):
        individuals, families = parse(GEDCOM_FILE)
        for indID in individuals:

            name, sex, birth, death, famsID, famcID = individuals[indID].get_individual()

            self.assertTrue(dates_before_current_date(birth, type="Birthday"))
            self.assertTrue(dates_before_current_date(death, type="Deathday"))
            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                divorce = families[fam].get_divorce_date()
                self.assertTrue(dates_before_current_date(marriage, type="Marriage"))
                self.assertTrue(dates_before_current_date(divorce, type="Divorce"))

    def test_birth_before_marriage(self):
        individuals, families = parse(GEDCOM_FILE)
        for indID in individuals:

            name, sex, birth, death, famsID, famcID = individuals[indID].get_individual()
            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                self.assertTrue(birth_before_marriage(birth, marriage))

    def test_birth_before_death(self):
        individuals, families = parse(GEDCOM_FILE)
        for indID in individuals:

            name, sex, birth, death, famsID, famcID = individuals[indID].get_individual()
            self.assertTrue(birth_before_death(birth, death))

    def test_marriage_before_divorce(self):

        individuals, families = parse(GEDCOM_FILE)
        for indID in individuals:
        
            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                divorce = families[fam].get_divorce_date()
                self.assertTrue(marriage_before_divorce(marriage, divorce))

    def test_marriage_before_death(self):
        individuals, families = parse(GEDCOM_FILE)
        
        for indID in individuals:
            name, sex, birth, death, famsID, famcID = individuals[indID].get_individual()
            fams = individuals[indID].get_famsID()
            for fam in fams:
                marriage = families[fam].get_marriage_date()
                self.assertTrue(marriage_before_death(marriage, death))

    def test_divorce_before_death(self):
        individuals, families = parse(GEDCOM_FILE)
        
        for indID in individuals:
            name, sex, birth, death, famsID, famcID = individuals[indID].get_individual()
            fams = individuals[indID].get_famsID()
            for fam in fams:
                divorce = families[fam].get_divorce_date()
                self.assertTrue(divorce_before_death(divorce, death))

    def test_less_then_150_years_old(self):
        individuals, families = parse(GEDCOM_FILE)
        
        for indID in individuals:
            age = individuals[indID].get_age().years
            self.assertTrue(less_then_150_years_old(age))

if __name__ == '__main__':
    unittest.main()

