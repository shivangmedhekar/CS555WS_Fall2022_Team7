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
    #                               Helper Functions                               #
    # ---------------------------------------------------------------------------- #
    def get_age(self):

        diff = datetime.now() if (self.get_death_date() == None) else self.get_death_date()
        age = relativedelta(diff, self.get_birth_date())
        return age

    def is_alive(self):
        
        if self.get_death_date() == None:
            return False
        else:
            return True