#Feiertag.py
from datetime import date, timedelta
jahr = int(input("Welches Jahr?" ))
print("Feirtage im Jahr", jahr, "im Bundesland Berlin")
neu = date(jahr, 1, 1)
A = jahr%19
K = jahr//100
M = 15+(3*K+3)//4-(8*K+13)//25
D = (19*A+M)%30
S = 2-(3*K+3)//4
R = D//29+(D//28-D//29)*(A//11)
OG = 21+D+R
SZ = 7-(jahr+jahr//4+S)%7
OE = 7-(OG-SZ)%7
OS = (OG+OE)
if OS>31:
    tag = OS-31
    monat = 4 
    ostern = date(jahr,monat,tag)
else:
    tag = OS
    monat = 3
    ostern = date(jahr,monat,tag)
print("Neujahr:\t\t\t", neu)
print("Frauentag:\t\t\t", date(jahr,3,8))
print("Karfreitag:\t\t\t", ostern - timedelta(days=2))
print("Osternsonntag:\t\t\t", ostern)
print("Tag der Arbeit:\t\t\t", date(jahr,5,1))
print("Christi Himmelfahr:\t\t", ostern - timedelta(days=-39))
print("Pfingsmontag:\t\t\t", ostern - timedelta(days=-50))
print("Tag der deutschen Einhaeit:\t", date(jahr,10,3))
print("1. Weinachtsfeirtag:\t\t", date(jahr,12,25))
print("2. Weinachtsfeirtag:\t\t", date(jahr,12,26))
input("Beenden mit Eingabetaste")
