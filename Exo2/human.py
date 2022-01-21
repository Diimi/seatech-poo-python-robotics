import time
class Human():

    _sexe='<unknown>'
    _mon_estomac = []

    def __init__(self,sexe):

        self._sexe = sexe
    

    def eat(self, aliments):
        if type(aliments)== str:
            print("Mmmm, Vous avez mangé : " , aliments)
            time.sleep(1)
            self.mon_estomac.append(aliments)

        else : 

            for i in aliments:
                print("WAA, vous avez mangé : %s  " %i)
                time.sleep(1)
                self.mon_estomac.append(i)

    def digest(self):
        print("Je suis en pleine digestion : " , self._mon_estomac )
        pass

    def dormir(self):
        
        pass
    
    @property
    def sexe(self):
        return self._sexe

    @property
    def mon_estomac(self):
        return self._mon_estomac
        
        
        