class Kunde:
    def __init__(self,vn,nn,nu):
        self.__name= vn
        self.__surname= nn
        self.__number=nu

    def setName(self, str):
        self.__name= str

    def getName(self):
        return self.__name

    def setSurname(self, str):
        self.__surname= str

    def getSurname(self):
        return self.__surname

    def setNumber(self, int):
        self.__number= int

    def getNumber(self):
        return self.__number

    def getType(self):
        return "Kunde"