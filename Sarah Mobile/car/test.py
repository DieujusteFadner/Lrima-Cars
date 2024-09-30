import RPi.GPIO as GPIO
import time

# Ultrasonic sensor pins
TRIG_FRONT = 4
ECHO_FRONT = 10
TRIG_BACK = 23
ECHO_BACK = 24


# Motor pins
motor1A = 9
motor1B = 25
enable1 = 11  # Motor 1 enable pin (PWM)
motor2A = 22
motor2B = 27
enable2 = 17  # Motor 2 enable pin (PWM)

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_FRONT, GPIO.OUT)
GPIO.setup(ECHO_FRONT, GPIO.IN)
GPIO.setup(TRIG_BACK, GPIO.OUT)
GPIO.setup(ECHO_BACK, GPIO.IN)
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(enable1, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)
GPIO.setup(enable2, GPIO.OUT)

# Initialize PWM for motor enable pins
pwm_motor1 = GPIO.PWM(enable1, 100)  # Initialize PWM with a frequency of 100Hz
pwm_motor2 = GPIO.PWM(enable2, 100)  # Initialize PWM with a frequency of 100Hz
pwm_motor1.start(0)  # Start PWM with a duty cycle of 0 (off)
pwm_motor2.start(0)  # Start PWM with a duty cycle of 0 (off)

# Function to measure distance with ultrasonic sensor
def measure_distance(trig_pin, echo_pin):
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
    return distance_cm

# Function to move the robot car backward
def move_backward(speed):
    GPIO.output(motor1A, GPIO.HIGH)  # Reverse motor 1
    GPIO.output(motor1B, GPIO.LOW)   # Reverse motor 1
    GPIO.output(motor2A, GPIO.HIGH)  # Reverse motor 2
    GPIO.output(motor2B, GPIO.LOW)   # Reverse motor 2
    pwm_motor1.ChangeDutyCycle(speed)
    pwm_motor2.ChangeDutyCycle(speed)
    print("Moving Backward")

# Function to move the robot car forward
def move_forward(speed):
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)
    pwm_motor1.ChangeDutyCycle(speed)
    pwm_motor2.ChangeDutyCycle(speed)
    print("Moving Forward")

# Function to turn the robot car left
def turn_left(speed):
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)
    pwm_motor1.ChangeDutyCycle(30)
    pwm_motor2.ChangeDutyCycle(speed)
    print("Turning Left")

# Function to turn the robot car right
def turn_right(speed):
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)
    pwm_motor1.ChangeDutyCycle(speed)
    pwm_motor2.ChangeDutyCycle(30)
    print("Turning Right")

# Function to stop the robot car
def stop():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.LOW)
    pwm_motor1.ChangeDutyCycle(0)  # Stop motor 1
    pwm_motor2.ChangeDutyCycle(0)  # Stop motor 2
    print("Stopping")

try:
    
    while True:
        # Measure distances from sensors
        front_distance = measure_distance(TRIG_FRONT, ECHO_FRONT)
        back_distance = measure_distance(TRIG_BACK, ECHO_BACK)
        speed = 70
        stopping_distance = 20
        
        # Print distances
        print("Front Distance:", front_distance, "cm")
        print("back Distance:", back_distance, "cm")
        if front_distance <= stopping_distance:
            stop()
            time.sleep(1)
            move_backward(speed)
            time.sleep(1)
            turn_left(speed)
            time.sleep(1)
            move_forward(speed)
        elif back_distance <= stopping_distance:
            stop()
            time.sleep(1)
            turn_left(speed)
            time.sleep(1)
            move_forward(speed)
        else:
            move_forward(speed)
        
except KeyboardInterrupt:
    stop()
    GPIO.cleanup()
