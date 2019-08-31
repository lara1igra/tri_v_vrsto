ZMAGA_X = "Zmagal je križec."
ZMAGA_O = "Zmagal je krožec."
NI_ZMAGE = "NZ"
POLJE_ZASEDENO = "Polje je zasedeno!"
NEVELJAVNA_VRSTICA_STOLPEC = "Neveljavna vrstica/stolpec"

import json

class TriVVrsto:
    def __init__(self, datoteka_z_potezami):
        self.seznam = []
        self.datoteka_z_potezami = datoteka_z_potezami
        self.trenutni_igralec = ""
        self.nalozi()

        
    def nova_igra(self):
        
        self.seznam = ["prazno", "prazno", "prazno", "prazno", "prazno", "prazno", "prazno", "prazno", "prazno"]
        self.trenutni_igralec = "krizec"
        self.shrani()

    def preveri_zmago(self):
        
        # preveri vrstice
        if ("krizec" == self.seznam[0] and "krizec" == self.seznam[1] and "krizec" == self.seznam[2]):
            return ZMAGA_X
        if ("krizec" == self.seznam[3] and "krizec" == self.seznam[4] and "krizec" == self.seznam[5]):
            return ZMAGA_X
        if ("krizec" == self.seznam[6] and "krizec" == self.seznam[7] and "krizec" == self.seznam[8]):
            return ZMAGA_X

        if ("krozec" == self.seznam[0] and "krozec" == self.seznam[1] and "krozec" == self.seznam[2]):
            return ZMAGA_O
        if ("krozec" == self.seznam[3] and "krozec" == self.seznam[4] and "krozec" == self.seznam[5]):
            return ZMAGA_O
        if ("krozec" == self.seznam[6] and "krozec" == self.seznam[7] and "krozec" == self.seznam[8]):   
            return ZMAGA_O

        # preveri stolpce
        if ("krizec" == self.seznam[0] and "krizec" == self.seznam[3] and "krizec" == self.seznam[6]):
            return ZMAGA_X
        if ("krizec" == self.seznam[1] and "krizec" == self.seznam[4] and "krizec" == self.seznam[7]):
            return ZMAGA_X
        if ("krizec" == self.seznam[2] and "krizec" == self.seznam[5] and "krizec" == self.seznam[8]):
            return ZMAGA_X

        if ("krozec" == self.seznam[0] and "krozec" == self.seznam[3] and "krozec" == self.seznam[6]):
            return ZMAGA_O
        if ("krozec" == self.seznam[1] and "krozec" == self.seznam[4] and "krozec" == self.seznam[7]):
            return ZMAGA_O
        if ("krozec" == self.seznam[2] and "krozec" == self.seznam[5] and "krozec" == self.seznam[8]):
            return ZMAGA_O

        # preveri diagonale
        if ("krizec" == self.seznam[0] and "krizec" == self.seznam[4] and "krizec" == self.seznam[8]):
            return ZMAGA_X
        if ("krizec" == self.seznam[2] and "krizec" == self.seznam[4] and "krizec" == self.seznam[6]):
            return ZMAGA_X

        if ("krozec" == self.seznam[0] and "krozec" == self.seznam[4] and "krozec" == self.seznam[8]):
            return ZMAGA_O
        if ("krozec" == self.seznam[2] and "krozec" == self.seznam[4] and "krozec" == self.seznam[6]):
            return ZMAGA_O
        
        self.shrani()

        return NI_ZMAGE

    def dodajKrizecAliKrozec(self, poteza): # ("1,2")
        # preveri ali je vrstica/stolpec pravilen
        
        if (len(poteza) != 3 or poteza[1] != ',' or int(poteza[0]) < 1 or int(poteza[0]) > 3 or int(poteza[2]) < 1 or int(poteza[2]) > 3):
            return NEVELJAVNA_VRSTICA_STOLPEC

        vrstica = poteza[0]
        stolpec = poteza[2]

        # preverimo ali so vsa polja že zasedena
        vsa_polja_zasedena = True
        for polje in self.seznam:
            if polje == "prazno":
                vsa_polja_zasedena = False
                break
        if vsa_polja_zasedena:
            return "Vsa polja so zasedena, igre je konec."


        # preveri ali je polje zasedeno, napolni polje z pravilno vrednostjo
        if (vrstica == "1" and stolpec == "1"):
            if self.seznam[0] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[0] = self.trenutni_igralec
        if (vrstica == "1" and stolpec == "2"):
            if self.seznam[1] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[1] = self.trenutni_igralec
        if (vrstica == "1" and stolpec == "3"):
            if self.seznam[2] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[2] = self.trenutni_igralec
        if (vrstica == "2" and stolpec == "1"):
            if self.seznam[3] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[3] = self.trenutni_igralec
        if (vrstica == "2" and stolpec == "2"):
            if self.seznam[4] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[4] = self.trenutni_igralec
        if (vrstica == "2" and stolpec == "3"):
            if self.seznam[5] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[5] = self.trenutni_igralec
        if (vrstica == "3" and stolpec == "1"):
            if self.seznam[6] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[6] = self.trenutni_igralec
        if (vrstica == "3" and stolpec == "2"):
            if self.seznam[7] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[7] = self.trenutni_igralec
        if (vrstica == "3" and stolpec == "3"):
            if self.seznam[8] != "prazno":
                return POLJE_ZASEDENO
            self.seznam[8] = self.trenutni_igralec

        # preveri zmago
        zmaga = self.preveri_zmago()

        if zmaga == NI_ZMAGE:
            if self.trenutni_igralec == "krizec":
                self.trenutni_igralec = "krozec"
                return "Na vrsti je krožec"
            else:
                self.trenutni_igralec = "krizec"
                return "Na vrsti je križec"
        else:
            return zmaga
        self.shrani()
        

    def nalozi(self):
        with open(self.datoteka_z_potezami, encoding='utf-8') as dat:
            slovar = json.load(dat)
            self.seznam = slovar['poteze_igre']
            self.trenutni_igralec = slovar['trenutni_igralec']
            
            

    def shrani(self):
        slovar = {
            'poteze_igre' : self.seznam,
            'trenutni_igralec' : self.trenutni_igralec,
        }
        print(self.dodajKrizecAliKrozec)
        with open(self.datoteka_z_potezami, 'w', encoding='utf-8') as dat:
            return json.dump(slovar, dat, ensure_ascii=False, indent=2)

    




