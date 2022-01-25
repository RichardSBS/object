class Fahrzeug:
    def __init__(self):
        self.__color=""
        self.__power=0
        self.__wheels=0

    def getSound(self):
        return("blub")

    def setColor(self,color):
        self.__color=color

    def setPower(self,power):
        self.__color=power

    def setWheels(self,wheels):
        self.__color=wheels

    def getColor(self):
        return self.__color

    def getWheels(self):
        return self.__wheels

    def getPower(self):
        return self.__power