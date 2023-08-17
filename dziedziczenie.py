class Szef:
    def __init__(self, poziom = None, imie=None):
        self.__poziom = poziom
        self.__imie = imie
        
    def set_poziom(self, poziom):
        self.__poziom = poziom
        
    def get_poziom(self):
        return self.__poziom
    
    def set_imie(self, imie):
        self.__imie = imie 
        
    def get_imie(self):
        return self.__imie

    poziom = property(fget = get_poziom, fset = set_poziom)
    imie = property(fget=get_imie, fset=set_imie)
 

#print(s1.get_imie(), s1.get_poziom())
#print(s2.get_imie(), s2.get_poziom())


    
class Konferencja:
    
    def __init__(self):
        self.__czlonkowie = []
    
    def dodaj_czlonka(self, czlonek):
        self.__czlonkowie.append(czlonek)

    def usun_czlonka(self, pozycja):
        self.__czlonkowie.pop(pozycja)

    def raport(self):
        for czlonek in self.__czlonkowie:
            print(f'Imie: {czlonek.imie} Poziom: {czlonek.poziom}')

k1 = Konferencja()
k1.dodaj_czlonka(Szef("JUREK", 50))
k1.dodaj_czlonka(Szef("JAN", 62))
k1.dodaj_czlonka(Szef("JANUSZ", 14))
k1.usun_czlonka(2)

k1.raport()  