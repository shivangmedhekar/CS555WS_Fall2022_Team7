# ---------------------------------------------------------------------------- #
#                               Class: Individual                              #
# ---------------------------------------------------------------------------- #
from dateutil.relativedelta import relativedelta
from datetime import datetime
from typing import List

class Individual:
    # -------------------------------- Constructor ------------------------------- #
    def __init__(self, ind_id: str, famc_id: List[str], fams_id: List[str],
                 name: str, sex: str, birth: datetime.date, death: datetime.date):
        """_summary_

        Args:
            ind_id (str): _description_
            famc_id (List[str]): _description_
            fams_id (List[str]): _description_
            name (str): _description_
            sex (str): _description_
            birth (datetime.date): _description_
            death (datetime.date): _description_
        """
        
        self.__ind_id = ind_id
        self.__famc_id = famc_id
        self.__fams_id = fams_id
        self.__name = name
        self.__sex = sex
        self.__birth = birth
        self.__death = death

    # ---------------------------------- Getters --------------------------------- #
    def get_ind_id(self) -> str:
        return self.__ind_id

    def get_fams_id(self) -> List[str]:
        return self.__fams_id

    def get_famc_id(self) -> List[str]:
        return self.__famc_id

    def get_name(self) -> str:
        return self.__name

    def get_gender(self) -> str:
        return self.__sex

    def get_birth_date(self) -> datetime.date:
        return self.__birth

    def get_death_date(self) -> datetime.date:
        return self.__death

    def get_individual(self) -> List:
        return self.__name, self.__sex, self.__birth, self.__death, self.__fams_id, self.__famc_id
    
    
    # ---------------------------------- Setters --------------------------------- #
    def set_ind_id(self, ind_id: str):
        self.__ind_id = ind_id
    
    def set_fams_id(self, fams_id: List[str]):
        self.__fams_id = fams_id

    def set_famc_id(self, famc_id: List[str]):
        self.__famc_id = famc_id

    def set_name(self, name: str):
        self.__name = name

    def set_gender(self, sex: str):
        self.__sex = sex

    def set_birth_date(self, birth_date: datetime.date):
        self.__birth = birth_date
    
    def set_death_date(self, death_date: datetime.date):
        self.__death = death_date

    
    # ----------------------------- Member Functions ----------------------------- #
    def get_age(self) -> relativedelta:
        """
        This function calculates the age of the Individual

        Returns:
            relativedelta: The age of the Individual
        """
        
        end_date = datetime.now() if (self.get_death_date() == None) else self.get_death_date()
        age = relativedelta(end_date, self.get_birth_date())
        return age


    def is_alive(self) -> bool:
        """
        Checks if an Individual is alive or not

        Returns:
            bool: True if alive else False
        """
        
        if self.get_death_date() == None:
            return True
        else:
            return False