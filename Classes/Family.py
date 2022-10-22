class Family:

    # -------------------------------- Constructor ------------------------------- #
    def __init__(self, famID, husband, wife, marriage_date, divorce_date, children):
        self.__famID = famID
        self.__husband = husband
        self.__wife = wife
        self.__marriage_date = marriage_date
        self.__divorce_date = divorce_date
        self.__children = children

    # ---------------------------------------------------------------------------- #
    #                             Retrieving Variables                             #
    # ---------------------------------------------------------------------------- #

    def get_famID(self):
        return self.__famID

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
