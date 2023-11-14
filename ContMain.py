from oop.cont_bancar import ContBancar

cont1 = ContBancar('Daniela S', 'RO001')
cont1 = ContBancar('Ovidiu S', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont1.alimentareCont(700)
cont1.alimentareCont(300)

cont1.plataCard(500)
cont1.plataCard(300)
cont2.plataCard(100)
cont2.plataCard(200)

cont1.interogareSold()
cont2.interogareSold()

# tema
# clasa angajat
#nume, prenume, salariu, vechime
# constructor: nume, prenume, salariu, functie, vechime
# metode:
# descriere salariu in fct de vechime
3actualizare vechime (param noua vechime)
    #self.vechime = nouavechime
#daca are vechime sub 5ani, marim cu 300, peste 5 ani 500
