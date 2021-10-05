import random
counter = 0
zahl = random.randint(1,100)
while counter < 6:
    antwort = int(input("Errate die gesuchte Zahl zwischen 1 und 100!\n"))


    counter = counter + 1
    print ("Versuch: ",counter)

    if antwort == zahl:
        print ("Gratulation! Du hast meinen Schatz gewonnen!")

    if antwort < zahl:
        print ("Zu niedrig, du Landratte!")

    if antwort > zahl:
        print ("Zu hoch!")
print ("Game Over!")
