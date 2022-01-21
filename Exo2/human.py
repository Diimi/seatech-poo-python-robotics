import time
class Human():

    _sexe='<unknown>'
    _mon_estomac = []
    
    

    def __init__(self,sexe):

        self._sexe = sexe
    

    def eat(self, aliments):
        if type(aliments)== str:
            print("Le cyborg est en train de manger : " , aliments)
            time.sleep(3)
            self.mon_estomac.append(aliments)
            

        else : 

            for i in aliments:
                print("Le cybord est en train de manger : %s  " %i)
                time.sleep(1)
                self.mon_estomac.append(i)
                
        

    def digest(self):
            if(len(self._mon_estomac)<=4):
                print("Le cybord est en état de faire sa digestion : " , self._mon_estomac )
                time.sleep(2)
            else :
                print("Erreur,le cyborg a trop mangé...")
       
    @property
    def sexe(self):
        return self._sexe

    @property
    def mon_estomac(self):
        return self._mon_estomac
    
   
        
        
        