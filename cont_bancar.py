class ContBancar:
    #constructor
    def __init__(self, titularCont, iban):
        #atribute, filduri
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0


    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari {self.incercari_activare}')
        print('-------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('card activat')
            self.activ = True
        else:
            print('Pin gresit')
            self.incercari_activare = self.incercari_activare + 1
            #self.incercari_activare+=1

    def alimentareCont(self, suma):
        self.salut()
        self.sold += suma
        print(f'ati alimentat {suma}')
        print(f'aveti in cont {self.sold}')

    def salut(self):
        print(f'Buna {self.titularCont}')

    def plataCard(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'ati cheltuit {suma}')
            print(f'aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')


