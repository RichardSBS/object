from Fahrzeuge.fahrzeug import Fahrzeug
from Fahrzeuge.auto import Auto
from Fahrzeuge.motorrad import Motorad

motorad1=Motorad()
auto1=Auto()
print(motorad1.getSound())
print(auto1.getSound())
auto1.setColor("weiß")
print(auto1.getColor())