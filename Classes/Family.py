class Family:
    _famID = None
    _husband = None
    _wife = None
    _marriageDate = None
    _divorceDate = None
    _children = []

    def __init__(self, famID, husband, wife, marriageDate, divorceDate, children):
        self._famID = famID
        self._husband = husband
        self._wife = wife
        self._marriageDate = marriageDate
        self._divorceDate = divorceDate
        self._children = children

    def get_family(self):
        return self._husband, self._wife, self._marriageDate, self._divorceDate, self._children