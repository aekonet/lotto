# coding: utf8
from random import randint
 
sechser = []
zahl, durchlauf, treffer, dreier, vierer, fuenfer = 0, 0, 0, 0, 0, 0
 
print ('''Deine Lotto - Simulation
------------------------
Bitte gib sechs Zahlen zwischen eins und 49 ein. Die Zahlen dürfen 
sich nicht wiederholen.''')
 
# --- Eingabe ---
while len(sechser) < 6:
    try:
        zahl = int(input(str(len(sechser)+1) + '. Zahl: ')) 
        if zahl in range(1,50) and zahl not in sechser:
            sechser.append(zahl)
        else:
            print ('Es muss eine Zahl zwischen 1 und 49 sein')
            if len(sechser)>0:
                print ('und sie darf sich nicht wiederholen!')
                print ('Folgende Zahlen hast du bereits getippt:'),
                for i in range(len(sechser)):
                    print (sechser[i]),
                print ('')
    except:
        print ('Es muss eine Zahl zwischen 1 und 49 sein')
        if len(sechser)>0:
            print ('und sie darf sich nicht wiederholen!')
            print ('Folgende Zahlen hast du bereits getippt:'),
            for i in range(len(sechser)):
                print (sechser[i]),
            print ('')
  
print ('Dein 6er: '),
for i in range(6):
    print (sorted(sechser)[i]),
print ('')
 
# --- Berechnung ---
while 1:
    zufall = []
    for i in range(6):
        while zahl in zufall or zahl == 0:
            zahl = randint(1,49)
        else:
            zufall.append(zahl)
    durchlauf += 1
     
    for i in range(6):
        if zufall[i] in sechser:
            treffer += 1
    if treffer == 3:
        dreier =+ 1
    elif treffer == 4:
        vierer += 1
    elif treffer == 5:
        fuenfer += 1
    elif treffer == 6:
        break
    treffer = 0
     
# --- Ausgabe ---
print ('------------------------')
print ('Du hast nach '+ str(durchlauf) +' "Spielen" einen 6er erzielt')
print ('Chance auf einen 3er:', float(100*dreier)/durchlauf, '%')
print ('Chance auf einen 4er:', float(100*vierer)/durchlauf, '%')
print ('Chance auf einen 5er:', float(100*fuenfer)/durchlauf, '%')
