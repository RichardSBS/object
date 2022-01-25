from Fahrzeuge.fahrzeug import Fahrzeug
class Motorad(Fahrzeug):
    def __init__(self):
        print("ein motorad fährt rum")
        super(Motorad, self).__init__()

    def getSound(self):
        return("bruuuuuuum")