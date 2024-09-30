import RPi.GPIO as GPIO
from time import sleep
from random import randint

# ____ Pin pour la voiture ___

class Car():
     def __init__(self):
          self.controle = True
          self.phare1 = 7
          self.phare2 = 8
          self.ENB = 17
          self.IN4 = 27
          self.IN3 = 22
          self.ENA = 11
          self.IN2 = 25
          self.IN1 = 9
          self.R = 16
          self.G = 0
          self.B = 19
          self.capteurDistance1 = 20
          self.capteurDistance2 = 21
          self.capteurDistance3 = 26
          self.servoPIN = 13

          GPIO.setwarnings(False) # Ignore warning for now
          GPIO.setmode(GPIO.BCM) # Use physical pin numbering 
          GPIO.setup(self.phare1, GPIO.OUT, initial=GPIO.LOW)#phare 1
          GPIO.setup(self.phare2, GPIO.OUT, initial=GPIO.LOW)#pahre 2
          GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.LOW) #ENB
          GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW) #IN4
          GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW) #IN3
          GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.LOW) #ENA
          GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW) #IN2
          GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW) #IN1
          GPIO.setup(self.R, GPIO.OUT, initial=GPIO.LOW) #R
          GPIO.setup(self.G, GPIO.OUT, initial=GPIO.LOW) #G
          GPIO.setup(self.B, GPIO.OUT, initial=GPIO.LOW) #B
          GPIO.setup(self.capteurDistance1, GPIO.IN) #capteur Distance 1
          GPIO.setup(self.capteurDistance2, GPIO.IN) #capteur Distance 2
          GPIO.setup(self.capteurDistance3, GPIO.IN) #capteur Distance 3
        
          GPIO.setup(self.servoPIN, GPIO.OUT)

          self.p = GPIO.PWM(self.servoPIN, 50) # GPIO 13 for PWM with 50Hz
          self.p.start(0)




     def lightsOff(self):
          print("eteindre lumiere")
          GPIO.output(self.phare1, GPIO.LOW)
          GPIO.output(self.phare2, GPIO.LOW)
          

     def lightsOn(self):
          print("allumer lumiere")
          GPIO.output(self.phare1, GPIO.HIGH)
          GPIO.output(self.phare2, GPIO.HIGH)


          

     def turn(self,angle):
          self.p.ChangeDutyCycle(angle)
     
     
     
     def stop(self):
          print("Stop")
          GPIO.output(self.ENB, GPIO.LOW)
          GPIO.output(self.ENA, GPIO.LOW)

     def forward(self):
          print("forward")
          GPIO.output(self.ENB, GPIO.HIGH)
          GPIO.output(self.ENA, GPIO.HIGH)
          GPIO.output(self.IN4, GPIO.LOW)
          GPIO.output(self.IN2, GPIO.LOW)
          GPIO.output(self.IN1, GPIO.HIGH)
          GPIO.output(self.IN3, GPIO.HIGH)
            
       
               
     def backward(self):
          print("backward")
          GPIO.output(self.ENB, GPIO.HIGH)
          GPIO.output(self.ENA, GPIO.HIGH)
          GPIO.output(self.IN4, GPIO.HIGH)
          GPIO.output(self.IN2, GPIO.HIGH)
          GPIO.output(self.IN1, GPIO.LOW)
          GPIO.output(self.IN3, GPIO.LOW)
    

     def turnRight(self):
          print("Right")
          self.turn(2.5)
          
     
     def turnLeft(self):
          print("Left")
          self.turn(12.5)
     
     def centerWheel(self):
          print("center")
          self.turn(7.5)
     


