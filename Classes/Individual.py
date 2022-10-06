from dateutil.relativedelta import relativedelta
from datetime import datetime

class Individual:
    _indID = None
    _famcID = None
    _famsID = None
    _name = None
    _sex = None
    _birth = None
    _death = None

    # -------------------------------- Constructor ------------------------------- #
    def __init__(self, indID, famcID, famsID, name, sex, birth, death):
        self._indID = indID
        self._famcID = famcID
        self._famsID = famsID
        self._name = name
        self._sex = sex
        self._birth = birth
        self._death = death

    # ---------------------------------------------------------------------------- #
    #                             Retrieving Variables                             #
    # ---------------------------------------------------------------------------- #
    def get_indID(self):
        return self._indID

    def get_famsID(self):
        return self._famsID

    def get_famcID(self):
        return self._famcID

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._sex

    def get_birthday(self):
        return self._birth

    def get_deathday(self):
        return self._death

    def get_individual(self):
        return self._name, self._sex, self._birth, self._death, self._famsID, self._famcID

    # ---------------------------------------------------------------------------- #
    #                               Helper Functions                               #
    # ---------------------------------------------------------------------------- #
    def get_age(self):

        diff = datetime.now() if (self.get_deathday == None) else self.get_deathday()
        age = relativedelta(diff, self.get_birthday())
        return age

    def is_alive(self):
        
        if self.get_deathday() == None:
            return False
        else:
            return True