# Lotto
import random, time
random.seed()
 
usernumbers = []
randomnumbers = []
draws = 0
dreier = 0
vierer = 0
fünfer = 0
 
print("Willkommen beim Lotto-Simulator!")
print("Sie werden nun dazu aufgefordert 6 Zahlen von 1 - 45 einzugeben.")
print("Bitte verwenden Sie nur ganze Zahlen und keine Doppelten.")
 
while (len(usernumbers) < 6):
    try:
        x = int(input("Bitte "+str(len(usernumbers)+1)+". Zahl eingeben.    "))
        if x < 1 or x > 45 or x in usernumbers:
            print("Bitte nur Zahlen im Bereich 1 - 45 und keine Doppelten Zahlen verwenden.")
            print("Sie werden nun erneut aufgefordert, eine Zahl einzugeben.")
        else:
            usernumbers.append(x)
            usernumbers.sort()
            if len(usernumbers) == 6:
                print("Ihre finalen Zahlen:",str(usernumbers))
            else:
                print("Ihre bisherigen Zahlen:",str(usernumbers))
             
    except:
        print("Bitte nur ganze Zahlen verwenden.")
        print("Sie werden nun erneut aufgefordert, eine Zahl einzugeben.")
 
starttime = time.time()
while True:
    y = random.randint(1,45)
    if y in randomnumbers:
        continue
    else:
        randomnumbers.append(y)
    if len(randomnumbers) == 6:
        randomnumbers.sort()
        #print(randomnumbers)
        draws = draws + 1
        joinednumbers = list(usernumbers + randomnumbers)
        if len(set(joinednumbers)) == 9:
            dreier = dreier + 1
        if len(set(joinednumbers)) == 8:
            vierer = vierer + 1
        if len(set(joinednumbers)) == 7:
            fünfer = fünfer + 1
        if len(set(joinednumbers)) == 6:
            break
        randomnumbers.clear()
        joinednumbers.clear()
 
endtime = time.time()
sekunden = round(endtime - starttime,2)
minuten = round(sekunden / 60,2)
stunden = round(minuten / 60,2)
drawspersec = round(draws / sekunden,2)
print(" ")
print("Gewonnen!")
print("Zahlen:",randomnumbers)
print("Nach", draws,"Ziehungen, in:", sekunden, "Sekunden.")
print("Das sind", minuten, "Minuten oder", stunden, "Stunden.")
print("Das entspricht", drawspersec, "Ziehungen pro Sekunde!")
print("Währenddessen hattest du", dreier,"mal drei Richtige,")
print(vierer, "mal vier Richtige und", fünfer, "mal fünf Richtige!")
print("Chance auf 3er: 1 zu",str(round(draws/dreier,2)),"/ 4er: 1 zu ",str(round(draws/vierer,2)))
print("Chance auf 5er: 1 zu",str(round(draws/fünfer,2)),"/ 6er: 1 zu ",str(draws))
