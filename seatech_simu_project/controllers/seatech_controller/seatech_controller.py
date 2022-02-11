
from controller import Robot, Motor , Camera, DistanceSensor
import time

__reconnaissance = False

class RobotMotor(Motor):
    def __init__(self,name):

        super().__init__(name) 
        self.setPosition(float('inf'))
        self.setVelocity(0)
        


class SeatechRobot(Robot,Camera, DistanceSensor):

    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor("left wheel motor")
        self.__rightMotor = RobotMotor("right wheel motor")
        
        self.camera = Camera("camera")
        self.camera.enable(TIME_STEP)
        self.camera.recognitionEnable(samplingPeriod=50)     
        self.camera.getImage()
        
  

    def run(self):
     self.__leftMotor.setVelocity(MAX_SPEED)
     self.__rightMotor.setVelocity(MAX_SPEED)

    def rotationG(self):

     self.__leftMotor.setVelocity(3)
     self.__rightMotor.setVelocity(0)

    
    def stop(self):

           self.__leftMotor.setVelocity(0)
           self.__rightMotor.setVelocity(0)

    def fuir(self):
     self.__leftMotor.setVelocity(-MAX_SPEED)
     self.__rightMotor.setVelocity(-MAX_SPEED)
     
     

    def rotationD(self):

     self.__leftMotor.setVelocity(0)
     self.__rightMotor.setVelocity(3)

  

    def detection(self):

       
        data = self.camera.getRecognitionObjects() 
        
        for obj in data :

             id = obj.get_id()            
             taille = obj.get_size_on_image()
             print(taille)

             if obj.get_colors() == [1, 0, 0] and taille[0]>11:                
                print("cible en vue")
                self.__reconnaissance = True
                print(self.__reconnaissance)
                
                self.fuir()
                

             else  :
                 
                 self.__reconnaissance = False
                 print(self.__reconnaissance)
                 self.rotationD()

    @property
    def reconnaissance(self):
        return self.__reconnaissance         
                

           


if __name__ == '__main__' :
    TIME_STEP = 64
    MAX_SPEED = 6.28

    # create the Robot instance.
    robot = SeatechRobot()

    robot.rotationD()
    

    while robot.step(TIME_STEP) != -1:
        robot.detection()
        
        pass