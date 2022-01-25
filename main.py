from verwaltung import Kunde
from verwaltung.vipKunde import VIPKunde
kundea=Kunde("karl","hans",20)
kundea.__name= "hans"
kundea.__surname= "held"
kundea.__number=1
kundea.setName("hans")
kundea.setSurname("wurst")
kundea.setNumber(12)
print(kundea.getName())
print(kundea.getSurname())
print(kundea.getNumber())
kundeb=VIPKunde("hans","bauer",4)
print (kundeb.getType())
print(kundeb.getSa())
kundeb.setSa("Bilbo")
print(kundeb.getSa())
