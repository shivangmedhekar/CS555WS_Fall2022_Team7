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

    def __init__(self, indID, famcID, famsID, name, sex, birth, death):
        self._indID = indID
        self._famcID = famcID
        self._famsID = famsID
        self._name = name
        self._sex = sex
        self._birth = birth
        self._death = death

    # retrieving variables
    def get_indID(self):
        return self._indID

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

    def get_age(self):

        diff = None
        if self.get_deathday == None:
            diff = datetime.now()

        else:
            diff = self.get_deathday

        return relativedelta(datetime.now(), self.get_birthday())

    def is_alive(self):
        if self.get_deathday() == None:
            return False
        else:
            return True