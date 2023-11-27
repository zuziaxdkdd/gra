from random import randint, choice

#---------------------------------POSTACIE-----------------------------

#info o postaci
def wyswietl_informacje_o_postaci(postac):
    print(f"\nWybralxs postac: {postac['imie']}")
    print(f"Zycie: {postac['zycie']}")
    print(f"Mana: {postac['mana']}")
    print(f"Atak1: {postac['atak1']}")
    print(f"Atak2: {postac['atak2']}")
    print(f"Mini opis: {postac['mini opis']}")

# pokaz postaci
dostepne_postaci = [
    {'imie': 'normalna postac npc', 'zycie': 100, 'mana': 100, 'atak1': 'od 5 do 10' , 'atak2': 'od 10 do 15', 'mini opis': 'ma nudne ataki i jest malo ciekawa\n atak1 - normalny cios reka\n atak2 - lepszy atak, zabiera 10 many'},
    {'imie': 'samurai', 'zycie': 110, 'mana': 80, 'atak1': 'od 7 do 12' , 'atak2': 'od 18 do 25', 'mini opis': 'jedyne co robi to atakuje mieczem oraz argumentami\n atak1 - cios mieczem\n atak2 - wyzwiska/arguemtny, zabiera 15 many'},
    {'imie': 'murzyn', 'zycie': 1, 'mana': 1, 'atak1': 1, 'atak2': 0, 'mini opis': 'jest z afryki\n atak1 - zwykly atak\n atak2 - zbyt biedny na drugi'},
    {'imie': 'sterydziaraz', 'zycie': 150, 'mana': 45, 'atak1': 'od 20 do 30', 'atak2': 'od 35 do 45', 'mini opis': 'zyje silownia, nie potrzebuje niczego do walki oprocz sterydow\n atak1 - cios w TWARZ\n atak2 - doladowanie sterydowe, zabiera 15 many'},
    {'imie': 'menel', 'zycie': 85, 'mana': 80, 'atak1': 'od 3 do 10', 'atak2': 'od 24 do 27', 'mini opis': 'rzuca butelkami i ogolnie smieciami ktore znajdzie\n atak1 - podrywy\n atak2 - atak butelka od piwa, zabiera 15 many'},
]

# wybor postaci przez gracza
print("Postacie do wyboru:")
for i in range(len(dostepne_postaci)):
    print(f"{i + 1}. {dostepne_postaci[i]['imie']}")

wybor = int(input("Wybierz numer postaci: "))

if 1 <= wybor <= len(dostepne_postaci):
    wybrana_postac = dostepne_postaci[wybor - 1]
    wyswietl_informacje_o_postaci(wybrana_postac)
else:
    print("Zly numer kolego")

# wybor imienia i info reszta
print("-"*40)
imie = input('Podaj imie twojego bohatera: ')
zycie = ()
mana = ()


if wybor == 1:
    zycie = 100
    mana = 100
elif wybor == 2:
    zycie = 110
    mana = 80
elif wybor == 3:
    zycie = 1
    mana = 1
elif wybor == 4:
    zycie = 150
    mana = 45
elif wybor == 5:
    zycie = 85
    mana = 80

print(f"zycie {zycie}")
print(f"mana {mana}")


# -----------------------------------ATAKI-------------------------------


#-------dla npc-------

def normalny_cios_reka():
    return randint(5, 10)

def lepszy_atak():
    global mana
    if mana < 10:
        print("-"*40)
        print("Nie masz wystarczajacej ilosci many....niestety")
        return 0
    mana -= 10
    return randint(10, 15)

#def #atak na 4 lvl


#-------dla samuraia-------

def cios_mieczem_samuraia():
    return randint(7, 12)

def wyzwiska_samuraia():
    global mana
    if mana < 15:
        print("-"*40)
        print("Nie masz wystarczajacej ilosci many....niestety")
        return 0
    mana -= 15
    return randint(18, 25)

#def #atak na 4 lvl


#-------dla murzyna-------

def lekki_atak_jego_chudziutka_czarna_raczka():
    return 1

#def #atak na 4 lvl ale to jest imposible


#-------dla sterydziarz-------

def cios_w_TWARZ():
    return randint(20, 30)

def doladowanie_sterydowe():
    global mana
    if mana < 15:
        print("-"*40)
        print("Nie masz wystarczajacej ilosci many....niestety")
        return 0
    mana -= 15
    return randint(35, 45)


#-------dla menela-------

def podrywy():
    return randint(3, 10)

def atak_butelka_od_piwa():
    global mana
    if mana < 15:
        print("-"*40)
        print("Nie masz wystarczajacej ilosci many....niestety")
        return 0
    mana -= 15
    return randint(24, 27)


#------------wybor ataku przez gracza----------

if wybor == 1: #npc
    def wybierz_atak():
        print('a/A - normalny cios reka (od 5 do 10 obrazen)')
        print('b/B - lepszy atak (od 10 do 15 obrazen) (zabiera 10 many)')
        co = input().upper()
        if co == 'A':
            return normalny_cios_reka()
        elif co == 'B':
            return lepszy_atak()
        else:
            print("Nie wybrano akcji")
            return 0
        
elif wybor == 2: #samurai
    def wybierz_atak():
        print('a/A - cios mieczem (od 7 do 12 obrazen)')
        print('b/B - wyzwiska/argumenty (od 18 do 25 obrazen) (zabiera 15 many)')
        co = input().upper()
        if co == 'A':
            return cios_mieczem_samuraia()
        elif co == 'B':
            return wyzwiska_samuraia()
        else:
            print("Nie wybrano akcji")
            return 0
        
elif wybor == 3: #murzyn
    def wybierz_atak():
        print('a/A - zwykly atak (1 obrazenie)')
        co = input().upper()
        if co == 'A':
            return lekki_atak_jego_chudziutka_czarna_raczka()
        else:
            print("Nie wybrano akcji")
            return 0
        
elif wybor == 4: #sterydziarz
    def wybierz_atak():
        print('a/A - cios w TWARZ (od 20 do 30 obrazen)')
        print('b/B - doladowanie sterydowe (od 35 do 45 obrazen) (zabiera 15 many)')
        co = input().upper()
        if co == 'A':
            return cios_w_TWARZ()
        elif co == 'B':
            return doladowanie_sterydowe()
        else:
            print("Nie wybrano akcji")
            return 0
        
elif wybor == 5: #menel
    def wybierz_atak():
        print('a/A - podrywy (od 3 do 10 obrazen)')
        print('b/B - atak butelka od piwa (od 24 do 27 obrazen) (zabiera 15 many)')
        co = input().upper()
        if co == 'A':
            return podrywy()
        elif co == 'B':
            return atak_butelka_od_piwa()
        else:
            print("Nie wybrano akcji")
            return 0

# -------------------------------------OPONENTY------------------------------

def random_karzel():
    karly = [
        ["Karzel", 20, 5, 0],
        ["Karzel", 15, 3, 0],
    ]
    return choice(karly)


def random_koniara():
    koniary = [
        ["koniara", 20, 5, 0],
        ["koniara", 23, 4, 0],
    ]
    return choice(koniary)


def random_informatycy():
    informatycy = [
        ["grupa_informatykow", 25, 10, 0],
        ["grupa_informatykow", 30, 15, 0],
    ]
    return choice(informatycy)


def random_emosy():
    emosy = [
        ["emos", 30, 10, 0],
        ["emos", 35, 15, 0],
    ]
    return choice(emosy)  


def random_femboye():
    femboye = [
        ["femboy", 40, 18, 0],
        ["femboy", 45, 20, 0],
    ]
    return choice(femboye)  


def random_zodiakary():
    zodiakary = [
        ["zodiakary", 50, 20, 0],
        ["zodiakary", 52, 23, 0],
    ]
    return choice(zodiakary)  


def random_sigma():
    sigmaboss = [
        ["sigmafinalboss1", 80, 35, 0],
        ["sigmafinalboss2", 110, 28, 0],
    ]
    return choice(sigmaboss) 

# ---------------------------------------GRA----------------------------------

level = 1

#-------lvl 1-------


print("-"*40)
print("-"*40)
print("Poziom pierwszy. Idziesz sobie spokojnie ulica i nagle atakuje ciebie karzel.")
print("Probuje podskakiwac ale mu cos nie wychodzi. W kazdym razie walczysz;")

if zycie > 0: #walka z karlami, losuje jednego karla i z nim sie walczy
    karzel = random_karzel()
    print("-"*40)
    
    while karzel[1] > 0 and zycie > 0:
        print(" "*40)
        print(" "*40)
        print(f"{imie} walczy teraz z {karzel[0]}")
        print(f"Przeciwnik ma {karzel[1]} HP i zadaje Ci {karzel[2]} obrażeń")
        
       
        zycie -= karzel[2]
        if zycie <= 0:
            break


        print(f"Masz {zycie} HP i {mana} many")
        atak = wybierz_atak()
        karzel[1] -= atak
        print(f"Zadałeś {atak} obrażeń")


    if karzel[1] <= 0:
        print(" "*40)
        print(" "*40)
        print("-"*40)
        print('--Zabiłeś karla!!! ')
        print("--Skoro wygrales, otrzymujesz pelne odnowienie zdrowia i many!!")
        if wybor == 1:
            zycie = 100
            mana = 100
        elif wybor == 2:
            zycie = 110
            mana = 80
        elif wybor == 3:
            zycie = 1
            mana = 1
        elif wybor == 4:
            zycie = 150
            mana = 35
        elif wybor == 5:
            zycie = 85
            mana = 80
        
        print(f"Masz teraz {zycie} zycia i {mana} many")
    else:
        level = 0
        print("Przegrales....niestety")

#-------lvl 2-------

if level > 0:
    print("-"*40)
    print("-"*40)
    print("Poziom drugi. Jest piekna pogoda wiec idealna pora na pojscie do parku. Droga robi sie coraz wezsza. Niestety cos lub ktos ci ja blokuje.")
    print("Jest to koniara z kijem z glowa konia. Mowisz jej aby sie przesunela ale ona woli ciebie zaatakowac.")


    if zycie > 0:
        koniara = random_koniara()
        print("-"*40)
    
        while koniara[1] > 0 and zycie > 0:
            print(" "*40)
            print(" "*40)
            print(f"{imie} walczy teraz z {koniara[0]}")
            print(f"Przeciwnik ma {koniara[1]} HP i zadaje Ci {koniara[2]} obrażeń")
        
       
            zycie -= koniara[2]
            if zycie <= 0:
                break


            print(f"Masz {zycie} HP i {mana} many")
            atak = wybierz_atak()
            koniara[1] -= atak
            print(f"Zadałeś {atak} obrażeń")


        if koniara[1] <= 0:
            print(" "*40)
            print(" "*40)
            print("-"*40)
            print('--Zabiłeś koniare!!! ')
            print("-- Skoro wygrales, otrzymujesz pelne odnowienie zdrowia i many!!")
            if wybor == 1:
                zycie = 100
                mana = 100
            elif wybor == 2:
                zycie = 110
                mana = 80
            elif wybor == 3:
                zycie = 1
                mana = 1
            elif wybor == 4:
                zycie = 150
                mana = 35
            elif wybor == 5:
                zycie = 85
                mana = 80

            print(f"Masz teraz {zycie} zycia i {mana} many")
        else:
            level = 0
            print("Przegrales....niestety")



#-------lvl 3-------

if level > 0:
    print("-"*40)
    print("-"*40)
    print("Poziom trzeci. Zgubiles sie i nie wiesz gdzie jestes. Zauwazyles grupke osob niedaleko. Stwierdziles ze spytasz sie jak stad wyjsc.")
    print("Niestety okazalo sie ze to sa infromatycy i gadaja w jakims dziwnym jezyku;")
    print(" - Informatyk: 01101011 01101111 01101100 01100101 01100111 01101111 00100000 01100011 01101111 00100000 01110100 01111001 00100000 01100011 01101000 01100011 01100101 01110011 01111010 00100000 01101111 01100100 00100000 01101110 01100001 01110011")
    print(" - Ty: Kolego o co ci chodzi")
    print(" - Informatyk do innych informatykow: 01000100 01100001 01110111 01100001 01101010 01100011 01101001 01100101 00100000 01110111 01100001 01101100 01101001 01101101 01111001 00100000 01100111 01101111")
    print("Gratuluje, zaatakowal cie gang informatykow")


    if zycie > 0:
        grupa_infromatykow = random_informatycy()
        print("-"*40)
    
        while grupa_infromatykow[1] > 0 and zycie > 0:
            print(" "*40)
            print(" "*40)
            print(f"{imie} walczy teraz z {grupa_infromatykow[0]}")
            print(f"Przeciwnik ma {grupa_infromatykow[1]} HP i zadaje Ci {grupa_infromatykow[2]} obrażeń")
        
       
            zycie -= grupa_infromatykow[2]
            if zycie <= 0:
                break


            print(f"Masz {zycie} HP i {mana} many")
            atak = wybierz_atak()
            grupa_infromatykow[1] -= atak
            print(f"Zadałeś {atak} obrażeń")


        if grupa_infromatykow[1] <= 0:
            print(" "*40)
            print(" "*40)
            print("-"*40)
            print('--Zabiłeś grupe informatykow!!! ')
            print("-- Skoro wygrales, otrzymujesz pelne odnowienie zdrowia i many!!")
            if wybor == 1:
                zycie = 100
                mana = 100
            elif wybor == 2:
                zycie = 110
                mana = 80
            elif wybor == 3:
                zycie = 1
                mana = 1
            elif wybor == 4:
                zycie = 150
                mana = 35
            elif wybor == 5:
                zycie = 85
                mana = 80

            print(f"Masz teraz {zycie} zycia i {mana} many")
        else:
            level = 0
            print("Przegrales....niestety")

#-------lvl 4-------

if level > 0:
    print("-"*40)
    print("-"*40)
    print("Poziom czwarty. Na szczescie orientujesz sie juz gdzie jestes. Niestety zaczelo padac. Na lono natury zaczely wychodzic emosy.")
    print("Zaatakowaly ciebie bez powodu.")


    if zycie > 0:
        emosy = random_emosy()
        print("-"*40)
    
        while emosy[1] > 0 and zycie > 0:
            print(" "*40)
            print(" "*40)
            print(f"{imie} walczy teraz z {emosy[0]}")
            print(f"Przeciwnik ma {emosy[1]} HP i zadaje Ci {emosy[2]} obrażeń")
        
       
            zycie -= emosy[2]
            if zycie <= 0:
                break


            print(f"Masz {zycie} HP i {mana} many")
            atak = wybierz_atak()
            emosy[1] -= atak
            print(f"Zadałeś {atak} obrażeń")


        if emosy[1] <= 0:
            print(" "*40)
            print(" "*40)
            print("-"*40)
            print('--Zabiłeś emosow!!! ')
            print("-- Skoro wygrales, otrzymujesz pelne odnowienie zdrowia i many!!")
            if wybor == 1:
                zycie = 100
                mana = 100
            elif wybor == 2:
                zycie = 110
                mana = 80
            elif wybor == 3:
                zycie = 1
                mana = 1
            elif wybor == 4:
                zycie = 150
                mana = 35
            elif wybor == 5:
                zycie = 85
                mana = 80
        
            print(f"Masz teraz {zycie} zycia i {mana} many")
        else:
            level = 0
            print("Przegrales....niestety")


#-------lvl 5-------

if level > 0:
    print("-"*40)
    print("-"*40)
    print("Poziom piaty. Jestes juz zmeczony ale zaczepia cie femboy. Pyta czy chcesz zobaczyc NIESPODZIANKE.")
    print("Az na tyle glupi nie jestes i odmawiasz. Kolega troche sie wkurzyl.")


    if zycie > 0:
        femboye = random_femboye()
        print("-"*40)
    
        while femboye[1] > 0 and zycie > 0:
            print(" "*40)
            print(" "*40)
            print(f"{imie} walczy teraz z {femboye[0]}")
            print(f"Przeciwnik ma {femboye[1]} HP i zadaje Ci {femboye[2]} obrażeń")
        
       
            zycie -= femboye[2]
            if zycie <= 0:
                break


            print(f"Masz {zycie} HP i {mana} many")
            atak = wybierz_atak()
            femboye[1] -= atak
            print(f"Zadałeś {atak} obrażeń")


        if femboye[1] <= 0:
            print(" "*40)
            print(" "*40)
            print("-"*40)
            print('--Zabiłeś femboya!!! ')
            print("-- Skoro wygrales, otrzymujesz pelne odnowienie zdrowia i many!!")
            if wybor == 1:
                zycie = 100
                mana = 100
            elif wybor == 2:
                zycie = 110
                mana = 80
            elif wybor == 3:
                zycie = 1
                mana = 1
            elif wybor == 4:
                zycie = 150
                mana = 35
            elif wybor == 5:
                zycie = 85
                mana = 80
        
            print(f"Masz teraz {zycie} zycia i {mana} many")
        else:
            level = 0
            print("Przegrales....niestety")



#-------lvl 6-------

if level > 0:
    print("-"*40)
    print("-"*40)
    print("Poziom szosty. Po ciezkim i przerazajacym dniu mozesz wkoncu isc spac. We snie nawiedzaja cie zodiakary. Dostaly sie tam przez ich manifestacje i medytacje.")
    print("Wspolczuje bardzo. Chcesz sie pozadnie wyspac wiec postanawiasz z nimi zawalczyc. Niestety na tym poziomie juz tak latwo nie jest. ")


    if zycie > 0:
        zodiakary = random_zodiakary()
        print("-"*40)
    
        while zodiakary[1] > 0 and zycie > 0:
            print(" "*40)
            print(" "*40)
            print(f"{imie} walczy teraz z {zodiakary[0]}")
            print(f"Przeciwnik ma {zodiakary[1]} HP i zadaje Ci {zodiakary[2]} obrażeń")
        
       
            zycie -= zodiakary[2]
            if zycie <= 0:
                break


            print(f"Masz {zycie} HP i {mana} many")
            atak = wybierz_atak()
            zodiakary[1] -= atak
            print(f"Zadałeś {atak} obrażeń")


        if zodiakary[1] <= 0:
            print(" "*40)
            print(" "*40)
            print("-"*40)
            print('--Zabiłeś zodiakary!!! ')
            print("-- Skoro wygrales, otrzymujesz pelne odnowienie zdrowia i many!!")
            if wybor == 1:
                zycie = 100
                mana = 100
            elif wybor == 2:
                zycie = 110
                mana = 80
            elif wybor == 3:
                zycie = 1
                mana = 1
            elif wybor == 4:
                zycie = 150
                mana = 35
            elif wybor == 5:
                zycie = 85
                mana = 80
        
            print(f"Masz teraz {zycie} zycia i {mana} many")
        else:
            level = 0
            print("Przegrales....niestety")



#-------lvl 7-------

if level > 0:
    print("-"*40)
    print("-"*40)
    print("Poziom siodmy. Rano przerwal ci sen dzwiek pukania do drzwi. Domyslales sie ze zbliza sie kolejna walke ale pomimo tego i tak otworzyles.")
    print("Byl to giga potezny sigma male. Cos tam gadal ale nie mogles sie skupic patrzac na jego budowe. Zaatakowal cie.")
    print("(PS. Jest to final boss ktory ma dwie wersje. Pierwszy ma wiecej ataku a drugi ma wiecej hp. Losowo dostaniesz jednego z nich.)")


    if zycie > 0:
        sigmaboss = random_sigma()
        print("-"*40)
    
        while sigmaboss[1] > 0 and zycie > 0:
            print(" "*40)
            print(" "*40)
            print(f"{imie} walczy teraz z {sigmaboss[0]}")
            print(f"Przeciwnik ma {sigmaboss[1]} HP i zadaje Ci {sigmaboss[2]} obrażeń")
        
       
            zycie -= sigmaboss[2]
            if zycie <= 0:
                break


            print(f"Masz {zycie} HP i {mana} many")
            atak = wybierz_atak()
            sigmaboss[1] -= atak
            print(f"Zadałeś {atak} obrażeń")


        if sigmaboss[1] <= 0:
            print(" "*40)
            print(" "*40)
            print("-"*40)
            print('--Zabiłeś bossa!!!!!!!!!!! ')
            print("-- Gratuluje ukonczenia gry!!!! ")
        else:
            level = 0
            print("Przegrales na final bossie. No coz i tak to daleki poziom....")



print("-"*40)
print("KONIEC GRY!")
