from pickle import TRUE
import time

class Robot():

    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
    def __init__(self):
      self.__name = ""
      self.__power = False
      self.__current_speed = 0
      self.__battery_level = 0
      
    

    def attributionNom(self):
      if(self.__power == "ON"):

        self.__name = input("Donne moi un nom : ")
        print("Je m'appelle " + self.__name+".")
        
      else :
        self.__power = False
        print("Vous devez démarrer le robot avant")


    def demarrageRobot(self):
      
      self.__power = input("Voulez vous allumer le robot ? (ON/OFF) : ")
      if(self.__power == "ON"): 
        print("Demarrage du robot")

    def ArretRobot(self):
      self.__power = input("Voulez vous éteindre le robot ? (ON/OFF) : ")
      if(self.__power == "OFF"):
        print("Arret du robot")

    def chargementRobot(self,batterie_level):
      print("Votre batterie est à " + str(batterie_level)+"%" )
      choix = input("Voulez vous charger le robot (O/N) : ")
      if(batterie_level !=100 and choix=="O"):
        print("Batterie en cours de chargement...")
        while batterie_level!=100:
              batterie_level +=1
              time.sleep(0.1)
              print(str(batterie_level)+ "%")
        
        print("Batterie chargée")
        
      else:
        print("Batterie déjà à 100%.")

    def vitesse_robot(self):
          self._current_speed = input("Rentrez une vitesse de déplacement : ")
          print("Votre vitesse est à : " + str(self._current_speed) +"km/h.")
    
    def arretdeplacement(self):
      arretrobot = input("Voulez vous arrêter le déplacement du robot ? (O/N) : ")
      if(arretrobot == "O"):
        print("Votre robot est arrété.")
    
    def resumeRobot(self,_name,_power,_batterie_level,_current_speed):
      resume = input("Voulez vous un résumé : (O/N) ")
      if(resume=="O"):
        print("Nom : " + str(_name))
        print("Current : " + str(_power))
        print("Niveau batterie" + str(_batterie_level))
        print("Vitesse actuelle " + str(_current_speed))


mon_Robot = Robot()

"Pour allumer son robot"
mon_Robot.demarrageRobot()

"Rentrez un nom dans le terminal"
mon_Robot.attributionNom()

"rentrez une valeure pour la batterie (par défault elle est initialisée à 0)"
mon_Robot.chargementRobot(50)

"Rentrez une vitesse"
mon_Robot.vitesse_robot()

"Pour arreter la vitesse du robot"
mon_Robot.arretdeplacement()

"POur avoir un résumé"


"POur arreter le robot"
mon_Robot.ArretRobot()


    

     