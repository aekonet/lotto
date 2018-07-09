from random import *

# random.seed()
j=1
anzahl = input("Anzahl: ")
datei = input("Dateiname: ")
d = open(datei,"a")

while j <= int(anzahl):
    
    def ziehung():
        zahlen = list(range(1,46))
        gezogen = []

        for i in range(6):
            zahl = randint(0, len(zahlen)-1)
            nmb = zahlen.pop(zahl)
            gezogen.append(nmb)
        return gezogen
    j = j+1
    ergebnis = ziehung()
    ergebnis.sort()
    for k in ergebnis:
        #print(str(k) + ";")
        d.write(str(k) + ";")
    #print("\n")
    d.write("\n")
d.close()




