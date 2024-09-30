import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # Import the sleep function from the time module



phare1 = 7
phare2 = 8
ENB = 17
IN4 = 27
IN3 = 22
ENA = 11
IN2 = 25
IN1 = 9
R = 16
G = 0
B = 19
capteurDistance1 = 20
capteurDistance2 = 21
capteurDistance3 = 26

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering 
GPIO.setup(phare1, GPIO.OUT, initial=GPIO.LOW)#phare 1
GPIO.setup(phare2, GPIO.OUT, initial=GPIO.LOW)#pahre 2
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW) #ENB
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW) #IN4
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW) #IN3
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW) #ENA
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW) #IN2
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW) #IN1
GPIO.setup(R, GPIO.OUT, initial=GPIO.LOW) #R
GPIO.setup(G, GPIO.OUT, initial=GPIO.LOW) #G
GPIO.setup(B, GPIO.OUT, initial=GPIO.LOW) #B
GPIO.setup(capteurDistance1, GPIO.IN) #capteurDistance1
GPIO.setup(capteurDistance2, GPIO.IN) #capteurDistance2
GPIO.setup(capteurDistance3, GPIO.IN) #capteurDistance3

servoPIN = 13
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 13 for PWM with 50Hz
p.start(0)

motor1 = GPIO.PWM(ENA,100)
motor2 = GPIO.PWM(ENB,100)
motor1.start(0)
motor1.start(0)

def detectObjectRight():
	isDetected = GPIO.input(capteurDistance1)
	return isDetected

def detectObjectLeft():
	isDetected = GPIO.input(capteurDistance2)
	return isDetected
	
def detectObjectFront():
	isDetected = GPIO.input(capteurDistance3)
	return isDetected
	
def forward(speed):
	GPIO.output(ENB, GPIO.HIGH)
	GPIO.output(ENA, GPIO.HIGH)
	GPIO.output(IN4, GPIO.HIGH)
	GPIO.output(IN2,  GPIO.HIGH)
	
	
def backward():
	GPIO.output(ENB, GPIO.HIGH)
	GPIO.output(ENA, GPIO.HIGH)
	GPIO.output(IN3, GPIO.HIGH)
	GPIO.output(IN1,  GPIO.HIGH)
	
	
def stop():
	GPIO.output(ENA, GPIO.LOW)
	GPIO.output(ENB, GPIO.LOW)
	

	
def turnRight():
	GPIO.output(ENB, GPIO.HIGH)
	GPIO.output(ENA, GPIO.HIGH)
	GPIO.output(IN3, GPIO.HIGH)
	GPIO.output(IN1, GPIO.LOW)
	GPIO.output(IN2, GPIO.HIGH)
	GPIO.output(IN4, GPIO.LOW)

def turnLeft():
	GPIO.output(ENB, GPIO.HIGH)
	GPIO.output(ENA, GPIO.HIGH)
	GPIO.output(IN3, GPIO.LOW)
	GPIO.output(IN1, GPIO.HIGH)
	GPIO.output(IN2, GPIO.LOW)
	GPIO.output(IN4, GPIO.HIGH)

	

def roule():
	while True:	
		if detectObjectFront() == 0:
			turnAngle(2.5)
			time.sleep(0.5)
			
		elif detectObjectLeft() == 0:
			turnAngle(13.5)
			time.sleep(0.5)
			
		elif detectObjectRight() == 0:
			turnAngle(2.5)
			time.sleep(0.5)
			
		else:
			forward()
			turnAngle(7.5)
			time.sleep(0.5)
		
		
forward()

