from dateutil.relativedelta import relativedelta
from datetime import datetime

class Individual:

    # -------------------------------- Constructor ------------------------------- #
    def __init__(self, ind_id, famc_id, fams_id, name, sex, birth, death):
        self.__ind_id = ind_id
        self.__famc_id = famc_id
        self.__fams_id = fams_id
        self.__name = name
        self.__sex = sex
        self.__birth = birth
        self.__death = death

    # ---------------------------------------------------------------------------- #
    #                             Retrieving Variables                             #
    # ---------------------------------------------------------------------------- #
    def get_ind_id(self):
        return self.__ind_id

    def get_fams_id(self):
        return self.__fams_id

    def get_famc_id(self):
        return self.__famc_id

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__sex

    def get_birth_date(self):
        return self.__birth

    def get_death_date(self):
        return self.__death

    def get_individual(self):
        return self.__name, self.__sex, self.__birth, self.__death, self.__fams_id, self.__famc_id
    
    # ---------------------------------------------------------------------------- #
    #                                    Setters                                   #
    # ---------------------------------------------------------------------------- #

    def set_fams_id(self, fams_id):
        self.__fams_id = fams_id

    def set_famc_id(self, famc_id):
        self.__famc_id = famc_id

    def set_name(self, name):
        self.__name = name

    def set_gender(self, sex):
        self.__sex = sex

    def set_birth_date(self, birth_date):
        self.__birth = birth_date
    
    def set_death_date(self, death_date):
        self.__death = death_date

    # ---------------------------------------------------------------------------- #
    #                               Helper Functions                               #
    # ---------------------------------------------------------------------------- #
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