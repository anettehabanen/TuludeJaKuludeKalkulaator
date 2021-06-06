#Autor: Anette Habanen
#Inimesed teevad igapäevaselt oste. Programm on loodud selleks, et aidata luua ülevaadet tehtud ostudest ning näidata võimalikke raha säästmise võimalusi.
#Programm küsib kasutajalt:
#•   millisest failist lugeda ostude summad ja kategooriad,
#•   kui palju taskuraha ta saab iga kuu (positiivne täisarv) ja
#•   mitu protsenti kuurahast ta soovib säästa.
#Programm väljastab ekraanile:
#•   kulutuste summa igas kategoorias ning kokku, 
#•   palju taskurahast üle on (kui kulutati rohkem kui taskraha oli, siis öeldakse, kui palju rohkem kulutati), 
#•   kui suur summa tahetakse ette antud protsendi põhjal säästa ja
#•   kui palju raha jääb üle taskurahast pärast ostude ja säästetava raha maha arvutamist.


from time import sleep

print("Tere!")
sleep(1)
print ("Olete asunud kasutama tulude ja kulude kalkulaatorit.")
sleep(1)
failinimi = input("Sisestage palun failinimi, kus on kirjas Teie sellekuised kulutused: ")

fail = open (failinimi, encoding = "UTF-8")
kulutused = []
for rida in fail:
    kulutused.append(rida)    # Failis olevad read loetakse järjendisse nimega kulutused.
fail.close()
    
summaS = 0
summaR = 0
summaM = 0
summaT = 0

def ostusumma (täht):            
    kulu = el.strip(täht)        # Funktsioon eemaldab ette antud failireast kategooriat tähistava tähe.
    ost = kulu.strip ("\n")      # Funktsioon eemaldab ette antud failirea lõpust reavahetuse.
    return ost 

for el in kulutused:
    if el.startswith("S"):                          # Ostud jaotatakse kategooriate järgi ära.
        summaS = summaS + float(ostusumma ("S"))    # Ühes kategoorias tehtud ostud liidetakse kokku.
    if el.startswith ("R"):
        summaR = summaR + float(ostusumma ("R"))
    if el.startswith ("M"):
        summaM = summaM + float(ostusumma ("M"))
    if el.startswith ("T"):
        summaT = summaT + float(ostusumma ("T"))
kokku = summaS + summaR + summaM + summaT           # Arvutatakse kõikide ostude summa kokku.
        
print ("")
print ("See kuu kulutasite söögi peale " + str(summaS) + " eurot.")          
print ("See kuu kulutasite riiete peale " + str(summaR) + " eurot.")
print ("See kuu kulutasite meelelahutuse peale " + str(summaM) + " eurot.")
print ("See kuu kulutasite transpordi peale " + str(summaT) + " eurot.")
print ("See kuu kulutasite kõikide asjade peale " + str(kokku) + " eurot.")

sleep(1)
print("")
kuuraha = int(input("Kui palju taskuraha Te saate iga kuu? "))     # Küsitakse taskuraha/kuuraha suurust.
üle = kuuraha - kokku                                              # Arvutatakse, kui palju raha jäi üle kuurahast
ülejääk = round(üle,2)

if ülejääk >= 0:
    print("Teil jäi taskurahast üle " + str(ülejääk) + " eurot.")
    sleep(1)
    print("")
    säästmiseprotsent = float(input("Mitu protsenti taskurahast Te sooviksite säästa? "))      # Tahetakse teada, mitu protsenti kuurahast tahetakse säästa ja kõrvale panna.
    säästmiseraha = säästmiseprotsent * 0.01 * kuuraha                                         # Antud protsendi põhjal arvutatakse rahasumma, mida sellisel juhul soovitakse säästa.
    print ("See tähendab, et soovite säästa " + str(round(säästmiseraha, 2)) + " eurot.")
    if säästmiseraha <= ülejääk :
        säästmisestüle = ülejääk - säästmiseraha                                               # Arvutatakse rahasumma, mis jääb üle, kui lahutada kuurahast maha kõik ostud ja rahasumma, mida tahetakse säästa.
        print ("See on võimalik ning Teile jääb veel üle " + str(round(säästmisestüle, 2)) + " eurot.")
    else:
        säästmisestpuudu = säästmiseraha - ülejääk                                             # Arvutatakse, mitu eurot inimene liiga palju kulutas, et ta ei saaks tahetud summat säästa.
        print ("Kahuks ei jäänud Teil see kuu nii palju raha üle, et selline summa säästa. Teil jääb säästmiseks vajalikust summast " + str(round(säästmisestpuudu,2)) + " eurot puudu.")
    
else:
    ülekuuraha = kokku - kuuraha                                                               # Arvutatakse, mitu eurot kuurahast kulutati rohkem 
    print("Kulutasite üle oma võimete ehk Te kulutasite " + str(ülekuuraha) + " eurot rohkem oma taskurahast.")
    

sleep(1)
print ("")
print ("Kena päeva jätku!")
print ("Loodame, et kasutate tulude ja kulude kalkulaatorit peagi jälle!")

