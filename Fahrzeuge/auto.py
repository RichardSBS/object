from Fahrzeuge.fahrzeug import Fahrzeug


class Auto(Fahrzeug):
    def __init__(self):
        print("ein Auto fährt rum")
        super(Auto, self).__init__()
        self.__doors=5
        self.__windows=6

    def getSound(self):
        return ("brumbrum")

    def setDoors(self,doors):
        self.__doors=doors

    def setWindows(self,windows):
        self.__windows=windows

    def getWindows(self):
        return self.__windows

    def getDoors(self):
        return self.__doors