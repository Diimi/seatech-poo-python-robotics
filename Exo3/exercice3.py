from abc import ABC, abstractmethod

_action = "inconnu"


class Animal(ABC):
    
    @abstractmethod
    def __init__(self,action):
        pass
    
    def alimentation(self):
        pass

    
class Voler():
        def __init__(self):
            print("- voler")
            

class Marcher():
        def __init__(self):
            print("- marcher")

class Nager():
    def __init__(self):
            print("- nager")


class Crocodile(Animal,Marcher,Nager):
    def __init__(self):
        print("Je suis un crocodile, je peux :")
        Marcher.__init__(self)
        Nager.__init__(self)
        print("**********************************")

    def faire_quelque_chose(self, action):
        print(f" Le crocodile est en train de {action}. ")
    
    def type_de_nourriture(self):
        print(" Je mange des humains")


class Lion(Animal):

    def __init__(self):
        print("Je suis un lion, je peux :")
        Marcher.__init__(self)
        print("**********************************")

    def faire_quelque_chose(self, action):
        print(f" Le lion est en train de {action}. ")

    def type_de_nourriture(self):
        print(" Je mange des gazelles")

class Pingouin(Animal):

    def __init__(self):
        print(" Je suis un pingouin, je peux :")
        Marcher.__init__(self)
        Nager.__init__(self)
        Voler.__init__(self)
        print("**********************************")

    def faire_quelque_chose(self, action):
        print(f" Le pingouin est en train de {action}. ")
    
    def type_de_nourriture(self):
        print(" Je mange des poissons")

class Carnivore():

        def alimentation(self):
            print("je suis carnivore")

class Herbivore():

        def alimentation(self):
            print("je suis herbivore")

      
zoo = [Lion(), Pingouin(), Crocodile()]

for animal in zoo:
    animal.faire_quelque_chose(action="manger")
    animal.type_de_nourriture()
    print("**********************************")
    

leopard = Carnivore()
pandas = Herbivore()

leopard.alimentation()
pandas.alimentation()





