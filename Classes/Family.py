# ---------------------------------------------------------------------------- #
#                                 Class: Family                                #
# ---------------------------------------------------------------------------- #
import datetime
from typing import List
class Family:

    # -------------------------------- Constructor ------------------------------- #
    def __init__(self, fam_id: str, husband: str, wife: str, marriage_date: datetime.date,
                 divorce_date: datetime.date, children: List[str]):
        """
        This is the constructor of class Family

        Args:
            fam_id (str): Unique ID of family
            husband (str): ID of husband from Individual Class
            wife (str): ID of wife from Individual Class
            marriage_date (datetime.date): Marriage date of husband and wife in the Family
            divorce_date (datetime.date): Divorce date of husband and wife in the Family
            children (List[str]): List of IDs of children of husband and wife in the Family
        """

        self.__fam_id = fam_id
        self.__husband = husband
        self.__wife = wife
        self.__marriage_date = marriage_date
        self.__divorce_date = divorce_date
        self.__children = children

    # ---------------------------------- Getters --------------------------------- #

    def get_fam_id(self):
        return self.__fam_id

    def get_husband(self):
        return self.__husband

    def get_wife(self):
        return self.__wife

    def get_marriage_date(self):
        return self.__marriage_date

    def get_divorce_date(self):
        return self.__divorce_date

    def get_children(self):
        return self.__children

    def get_family(self):
        return self.__husband, self.__wife, self.__marriage_date, self.__divorce_date, self.__children
    
    # ---------------------------------- Setters --------------------------------- #
    
    def set_fam_id(self, fam_id):
        self.__fam_id = fam_id

    def set_husband(self, husb_id):
        self.__husband = husb_id

    def set_wife(self, wife_id):
        self.__wife = wife_id
    
    def set_marriage_date(self, marriage_date):
        self.__marriage_date = marriage_date

    def set_divorce_date(self, divorce_date):
        self.__divorce_date = divorce_date

    def set_children(self, children):
        self.__children = children