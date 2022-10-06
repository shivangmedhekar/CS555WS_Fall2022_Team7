class Family:
    _famID = None
    _husband = None
    _wife = None
    _marriageDate = None
    _divorceDate = None
    _children = []

    # -------------------------------- Constructor ------------------------------- #
    def __init__(self, famID, husband, wife, marriageDate, divorceDate, children):
        self._famID = famID
        self._husband = husband
        self._wife = wife
        self._marriageDate = marriageDate
        self._divorceDate = divorceDate
        self._children = children

    # ---------------------------------------------------------------------------- #
    #                             Retrieving Variables                             #
    # ---------------------------------------------------------------------------- #

    def get_famID(self):
        return self._famID

    def get_husband(self):
        return self._husband

    def get_wife(self):
        return self._wife

    def get_marriage_date(self):
        return self._marriageDate

    def get_divorce_date(self):
        return self._divorceDate

    def get_children(self):
        return self._children

    def get_family(self):
        return self._husband, self._wife, self._marriageDate, self._divorceDate, self._children
