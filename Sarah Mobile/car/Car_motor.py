import RPi.GPIO as GPIO
import time
from aliot.aliot_obj import AliotObj

aliot = AliotObj("car")

class Car:

	def __init__(self, TRIG_FRONT = 4, ECHO_FRONT = 10, TRIG_BACK = 23, ECHO_BACK = 24, motor1A = 9, motor1B = 25, enable1 = 11, motor2A = 22, motor2B = 27, enable2 = 17, phare1 = 7, phare2 = 8, led_rouge = 16, led_verte = 0, led_bleu = 19):
		# Light pins  
		self.phare1 = phare1,
		self.phare2 = phare2,
		
		# Light pins  
		self.led_rouge = led_rouge
		self.led_verte = led_verte
		self.led_bleu = led_bleu
		
		# Ultrasonic pins
		self.TRIG_FRONT = TRIG_FRONT
		self.ECHO_FRONT = ECHO_FRONT
		self.TRIG_BACK = TRIG_BACK
		self.ECHO_BACK = ECHO_BACK
	

		# Motor pins
		self.motor1A = motor1A
		self.motor1B = motor1B
		self.enable1 = enable1  # Motor 1 enable pin (PWM)
		self.motor2A = motor2A
		self.motor2B = motor2B
		self.enable2 = enable2  # Motor 2 enable pin (PWM)
		
		# Initialize GPIO pins
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.TRIG_FRONT, GPIO.OUT)
		GPIO.setup(self.ECHO_FRONT, GPIO.IN)
		GPIO.setup(self.TRIG_BACK, GPIO.OUT)
		GPIO.setup(self.ECHO_BACK, GPIO.IN)
		
		GPIO.setup(self.motor1A, GPIO.OUT)
		GPIO.setup(self.motor1B, GPIO.OUT)
		GPIO.setup(self.enable1, GPIO.OUT)
		GPIO.setup(self.motor2A, GPIO.OUT)
		GPIO.setup(self.motor2B, GPIO.OUT)
		GPIO.setup(self.enable2, GPIO.OUT)
		GPIO.setup(self.phare1, GPIO.OUT)
		GPIO.setup(self.phare2, GPIO.OUT)
		
		# Initialize PWM for motor enable pins
		self.pwm_motor1 = GPIO.PWM(enable1, 100)  # Initialize PWM with a frequency of 100Hz
		self.pwm_motor2 = GPIO.PWM(enable2, 100)  # Initialize PWM with a frequency of 100Hz
		self.pwm_motor1.start(0)  # Start PWM with a duty cycle of 0 (off)
		self.pwm_motor2.start(0)  # Start PWM with a duty cycle of 0 (off)


	
	def move_forward(self,speed):
		GPIO.output(self.motor1A, GPIO.LOW)
		GPIO.output(self.motor1B, GPIO.HIGH)
		GPIO.output(self.motor2A, GPIO.LOW)
		GPIO.output(self.motor2B, GPIO.HIGH)
		self.pwm_motor1.ChangeDutyCycle(speed)
		self.pwm_motor2.ChangeDutyCycle(speed)
		print("Moving Forward")
	
	def move_backward(self, speed):
		GPIO.output(self.motor1A, GPIO.HIGH)  # Reverse motor 1
		GPIO.output(self.motor1B, GPIO.LOW)   # Reverse motor 1
		GPIO.output(self.motor2A, GPIO.HIGH)  # Reverse motor 2
		GPIO.output(self.motor2B, GPIO.LOW)   # Reverse motor 2
		self.pwm_motor1.ChangeDutyCycle(speed)
		self.pwm_motor2.ChangeDutyCycle(speed)
		print("Moving Backward")
			
		
	def turn_left(self, speed):
		GPIO.output(self.motor1A, GPIO.LOW)
		GPIO.output(self.motor1B, GPIO.HIGH)
		GPIO.output(self.motor2A, GPIO.LOW)
		GPIO.output(self.motor2B, GPIO.HIGH)
		self.pwm_motor1.ChangeDutyCycle(20)
		self.pwm_motor2.ChangeDutyCycle(speed)
		print("Turning Left")

	# Function to turn the robot car right
	def turn_right(self, speed):
		GPIO.output(self.motor1A, GPIO.LOW)
		GPIO.output(self.motor1B, GPIO.HIGH)
		GPIO.output(self.motor2A, GPIO.LOW)
		GPIO.output(self.motor2B, GPIO.HIGH)
		self.pwm_motor1.ChangeDutyCycle(speed)
		self.pwm_motor2.ChangeDutyCycle(20)
		print("Moving Forward")

		print("Turning Right")

	# Function to stop the robot car
	def stop(self, data):
		
		GPIO.output(self.motor1A, GPIO.LOW)
		GPIO.output(self.motor1B, GPIO.LOW)
		GPIO.output(self.motor2A, GPIO.LOW)
		GPIO.output(self.motor2B, GPIO.LOW)
		self.pwm_motor1.ChangeDutyCycle(0)  # Stop motor 1
		self.pwm_motor2.ChangeDutyCycle(0)  # Stop motor 2
		print("Stopping")
		
	def measure_distance(self, trig_pin, echo_pin):
		# Set Trigger to HIGH for 10us to trigger the sensor
		GPIO.output(trig_pin, True)
		time.sleep(0.00001)
		GPIO.output(trig_pin, False)

		# Measure the time between sending the signal and receiving the echo
		pulse_start = time.time()
		pulse_end = time.time()

		while GPIO.input(echo_pin) == 0:
			pulse_start = time.time()
			if (pulse_start - pulse_end) > 0.1: # If no response within 0.1s, return -1
				return -1

		while GPIO.input(echo_pin) == 1:
			pulse_end = time.time()
			if (pulse_end - pulse_start) > 0.1: # If no response within 0.1s, return -1
				return -1

		pulse_duration = pulse_end - pulse_start

		# Calculate distance using speed of sound (343m/s)
		distance_cm = pulse_duration * 34300 / 2

		if(distance_cm == -1):
			distance_cm = 0
		return float(f"{distance_cm:.2f}")

		
	def light_On(self, data):
		GPIO.output(self.phare1, GPIO.HIGH)
		GPIO.output(self.phare2, GPIO.HIGH)
		aliot.update_doc({"/doc/lights" : True})
		
	def light_Off(self, data):
		GPIO.output(self.phare1, GPIO.LOW)
		GPIO.output(self.phare2, GPIO.LOW)
		aliot.update_doc({"/doc/lights" : False})

	

				
