import RPi.GPIO as GPIO
from time import sleep
from random import randint

# ____ Pin pour la voiture ___

class Car():
     def __init__(self):
          self.controle = True
          self.ENA = 17
          self.ENB = 27
          self.IN1 = 22
          self.IN2 = 23
          self.IN3 = 24 
          self.IN4 = 25  
      

          GPIO.setwarnings(False) # Ignore warning for now
          GPIO.setmode(GPIO.BCM) # Use physical pin numbering 
          GPIO.setup(self.ENB, GPIO.OUT, initial=GPIO.LOW) #ENB
          GPIO.setup(self.IN4, GPIO.OUT, initial=GPIO.LOW) #IN4
          GPIO.setup(self.IN3, GPIO.OUT, initial=GPIO.LOW) #IN3
          GPIO.setup(self.ENA, GPIO.OUT, initial=GPIO.LOW) #ENA
          GPIO.setup(self.IN2, GPIO.OUT, initial=GPIO.LOW) #IN2
          GPIO.setup(self.IN1, GPIO.OUT, initial=GPIO.LOW) #IN1
         
        
        
          







     def controleManuel(self):
          GPIO.output(self.R, GPIO.HIGH)
          GPIO.output(self.G, GPIO.LOW)
          GPIO.output(self.B, GPIO.LOW)
          self.controle = True

     def controleAutomatique(self):
          GPIO.output(self.R, GPIO.LOW)
          GPIO.output(self.G, GPIO.HIGH)
          GPIO.output(self.B, GPIO.LOW)
          self.controle = False
 
     def stop(self):
          GPIO.output(self.ENB, GPIO.LOW)
          GPIO.output(self.ENA, GPIO.LOW)

     def forward(self):
          GPIO.output(self.ENB, GPIO.HIGH)
          GPIO.output(self.ENA, GPIO.HIGH)
          GPIO.output(self.IN3, GPIO.HIGH)
          GPIO.output(self.IN1, GPIO.HIGH)
          
        
     def backward(self, timed = False, timeout = 5):
          if timed:
               GPIO.output(self.ENB, GPIO.HIGH)
               GPIO.output(self.ENA, GPIO.HIGH)
               GPIO.output(self.IN1, GPIO.HIGH)
               GPIO.output(self.IN3, GPIO.HIGH)
               sleep(timeout)
               self.stop()
          else:
               GPIO.output(self.ENB, GPIO.HIGH)
               GPIO.output(self.ENA, GPIO.HIGH)
               GPIO.output(self.IN1, GPIO.HIGH)
               GPIO.output(self.IN3, GPIO.HIGH)

     def turnRight(self):
          self.turn(13.3)
          self.forward()
     
     def turnRight(self):
          self.turn(2.7)
          self.forward()
     
     def sendPosition(self):
          x = randint(1,4)
          y = randint(1,4)
          
          return x,y
