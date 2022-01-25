from verwaltung.kunde import Kunde
class VIPKunde(Kunde):

    def __init__(self,vn,nn,nu):
        print("ein VIPKunde wurde erschaffen")
        super(VIPKunde,self).__init__(vn,nn,nu)
        self.__Sachbearbeiter="Hans"
        self.VIP=True

    def setSa(self,str):
        self.__Sachbearbeiter=str

    def getSa(self):
        return self.__Sachbearbeiter

    def getType(self):
        return "VIPKunde"