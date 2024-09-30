from aliot.aliot_obj import AliotObj
from Car_motor import Car
from time import sleep

# CrÃ©ation de l'objet Ã  partir du fichier de configuration
car = AliotObj("car")
motor = Car()

def start():
    while True:
        front_distance = measure_distance(TRIG_FRONT, ECHO_FRONT)
        back_distance = measure_distance(TRIG_BACK, ECHO_BACK)
        print(front_distance, back_distance)
        car.update_doc({
            "front": front_distance,
            "back" : back_distance
        })
        
      
        sleep(1)
        
    # Ã‰crivez le code que vous voulez exÃ©cuter une fois que l'objet
    # est connectÃ© au serveur
    pass


# Appel de la fonction start une fois que l'objet se connecte au 
car.on_start(start)
car.on_action_recv(action_id="forward",callback=motor.move_forward)
car.on_action_recv(action_id="backward",callback=motor.move_backward)
car.on_action_recv(action_id="right",callback=motor.turn_right)
car.on_action_recv(action_id="left",callback=motor.turn_left)
car.on_action_recv(action_id="stop",callback=motor.stop)
car.on_action_recv(action_id="lightOn",callback=motor.light_On)
car.on_action_recv(action_id="lightOff",callback=motor.light_Off)

# Connection de l'objet au serveur ALIVEcode
car.run()
