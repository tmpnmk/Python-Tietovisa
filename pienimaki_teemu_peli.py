# Moon Etelä-Pohojalaane -Tietovisa
# 2019 (C) Teemu Pienimäki

import sys # exit
import time # sleep
import random # sample
clear = "\n" * 100 # Tyhjentää ruudun
pisteet = 0
oikein = "\nSoot oikias, pannaha 2 pistestä plakkarihi!\n"
vaarin = "\nSoot vääräs, motan 1 pistehen poies!\n"
nolla = "\nSoot vääräs!\n" # Tulostaa jos pistesaldo jo valmiiksi 0

# Tulostaa säännöt ja aloitusvalikon
def aloitus():
    print(clear)
    print("\nMOON ETELÄ-POHOJALAANE -TIETOVISA\n\nCopyright 2019 Teemu Pienimäki")
    time.sleep(3)
    print("\n\nSelevitetähä 10 kysymyksen avuulla, kuinka eteläpohojalaane soot muka.")
    time.sleep(3)
    print("\nOikiasta vastahuksesta saat 2 pistestä, väärästä miinustetaha 1 pistes.")
    time.sleep(3)
    print("\nKysymykset ja vastausvaihtoeheroot esitetähä satunnaases järiestykses.")
    time.sleep(3)
    print("\nLopus sulle tierootetaha kuinka eteläpohojalaane sookkaa. Ristus notta!")
    time.sleep(3)
    print("\n\n1 - Aloota\n\n2 - Pane pois")
    i = 0
    try:
        i = int(input("\nValittetaha (1-2): "))
    except ValueError:
        print("\nVirhe, sun pitääs panna kokonaasluku (1-2), ohojelma lopetetaha.\n")
        sys.exit()
    if i == 1:
        return
    if i == 2:
        print("\nPannaha poies, Häjyypoika!\n")
        sys.exit()
    if i >= 3:
        print("\nVirhe, sun pitääs panna kokonaasluku (1-2), ohojelma lopetetaha.\n")
        sys.exit()

# Arpoo kysymyksien numerot satunnaiseen järjestykseen
def kysymykset_sekaisin(lista):
    kysymykset = random.sample(lista, 10)
    return kysymykset
    
# Tulostaa kysymyksen, sekoittaa vastausvaihtoehdot, arvo a = oikea vastaus ja hallinnoi pistesaldoa
def kysymys(kysymys, vaihtoehdot, a, b, c, pisteet):
    sekoita = random.sample(vaihtoehdot, 3)
    print(clear)
    print("\nMOON ETELÄ-POHOJALAANE -TIETOVISA")
    time.sleep(3)
    print(kysymys)
    time.sleep(5)
    print(sekoita[0])
    time.sleep(2)
    print(sekoita[1])
    time.sleep(2)
    print(sekoita[2])
    time.sleep(3)
    i = 0
    try:
        i = int(input("\nVastataha (1-3): "))
    except ValueError:
        print("\nVirhe, sun pitääs panna kokonaasluku (1-3), ohojelma lopetetaha.\n")
        sys.exit()
    if i == a:
        print(oikein)
        pisteet += 2
        time.sleep(3)
    if i == b or i == c:
        if pisteet <= 1:
            print(nolla)
            pisteet = 0
        else:
            print(vaarin)
            pisteet -= 1
        time.sleep(3)
    if i >= 4:
        print("\nVirhe, sun pitääs panna kokonaasluku (1-3), ohojelma lopetetaha.\n")
        sys.exit()
    return pisteet

# Muuttaa pisteet prosenteiksi
def pisteet_prosenteiksi(p):
    prosentti = (100 / 20) * p
    return prosentti

# Lopetusruutu kertoo saadun prosentin
def lopetus():
    print(clear)
    arvosana = pisteet_prosenteiksi(pisteet)
    print("\nMOON ETELÄ-POHOJALAANE -TIETOVISA\n")
    time.sleep(3)
    if arvosana == 0:
        print("Ei sustoo rehriks eteläpohojalaaseks!\n")
        sys.exit()
    else:
        counter = 0
        while counter < arvosana:
            time.sleep(0.15)
            counter += 1
            print("Herrassiunaa! Soot", counter, end = " rosenttisesti rehti eteläpohojalaane!\r")
    print("\n")
    sys.exit()

# Kutsutaan valoitusvalikko
aloitus()

# Tulostaa 10 kysymysta satunnaisessa järjestyksessä
kysymykset = kysymykset_sekaisin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for n in kysymykset:

    if n == 1:
        pisteet = kysymys("\nMihinä krannis sijaattoo Lakeuren Risti?",["\n1 - Seinäjoki", "\n2 - Kauhava", "\n3 - Jalasjärvi"], 1, 2, 3, pisteet)

    if n == 2:
        pisteet = kysymys("\nSuupohojan pääkranni on...",["\n1 - Ilmajoki", "\n2 - Kauhajoki", "\n3 - Ylihärmä"], 2, 1, 3, pisteet)
      
    if n == 3:
        pisteet = kysymys("\nTieräkkö notta Teuvalla lymyylöö...",["\n1 - Pirunpesä", "\n2 - Susiluola", "\n3 - Horo"], 3, 1, 2, pisteet)
     
    if n == 4:
        pisteet = kysymys("\nLapualaaset rehvasteloo vuorellansa, joka tunnetaha nimellä...",["\n1 - Iso-Kakkori", "\n2 - Simpsiö", "\n3 - Lauhanvuori"], 2, 1, 3, pisteet)
  
    if n == 5:
        pisteet = kysymys("""\nEteläpohojammaan murtehella "tuoli" on...""",["\n1 - Kooli", "\n2 - Fletares", "\n3 - Lavitta"], 3, 1, 2, pisteet)
        
    if n == 6:
        pisteet = kysymys("""\nKenen Kurikkalaasen turvasta tuloo: "Eihä tällaasilla seipähillä hiihrä sonnikaa!"?""",["\n1 - Mieroon Jussin", "\n2 - Isoontaloon Antin", "\n3 - Kotipellon Timon"], 1, 2, 3, pisteet)

    if n == 7:
        pisteet = kysymys("\nMihinä pitäjäs tv-hahmo Tarjoushaukka lentelöö?",["\n1 - Karijoen Myrkyssä", "\n2 - Alavuden Tuurissa", "\n3 - Nurmoon Alapäässä"], 2, 1, 3, pisteet)
    
    if n == 8:
        pisteet = kysymys("\nLappajärvi on syntyny...",["\n1 - Tulivuoren kraaterista", "\n2 - Patoamalla tekojärveksi", "\n3 - Meteoriitin törmäyksestä"], 3, 1, 2, pisteet)
        
    if n == 9:
        pisteet = kysymys("\nRauhanajan yksi tuhoisimmista onnettomuuksista, patruunatehtahan räjährys 1976, tapahtui...",["\n1 - Lapualla", "\n2 - Kauhajoella", "\n3 - Alajärvellä"], 1, 2, 3, pisteet)
        
    if n == 10:
        pisteet = kysymys("""\nEteläpohojammaan murtehella "satula" on...""",["\n1 - Krävöö", "\n2 - Puo", "\n3 - Lesta"], 3, 1, 2, pisteet)

# Kutsutaan lopetus
lopetus()
