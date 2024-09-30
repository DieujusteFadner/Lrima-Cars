from car_utils import Car
import RPi.GPIO as GPIO

servoPIN = 13


GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 13 for PWM with 50Hz
p.start(0)
p.ChangeDutyCycle(7.5)
