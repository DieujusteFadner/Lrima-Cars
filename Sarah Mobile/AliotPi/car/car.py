import multiprocessing
from aliot.aliot_obj import AliotObj
from stream_utils import Stream
from car_utils import Car
from time import sleep


car = Car()
carALiot = AliotObj("car")
ip_address = Stream.get_ip_address()

linkStream = "https://" + ip_address + ":8080/video"


def start():
    listePosition = [[2.25, 1.75], # (milieu route)
            [2.50, 1.75],
            [2.75, 1.75],
            [3.00, 1.75],
            [3.25, 1.75],
            [3.50, 1.75],
            [3.75, 1.75],
            [4.00, 1.75],
            [4.25, 1.75], # (haut droite)
            [4.25, 2.00],
            [4.25, 2.25],
            [4.25, 2.50],
            [4.25, 2.75],
            [4.25, 3.00],
            [4.25, 3.25],
            [4.25, 3.50],
            [4.25, 3.75],
            [4.25, 4.00],
            [4.25, 4.25], # (bas droite)
            [4.00, 4.25], 
            [3.75, 4.25],
            [3.50, 4.25], 
            [3.25, 4.25], # (stop)
            [3.00, 4.25], 
            [2.75, 4.25],
            [2.50, 4.25], 
            [2.25, 4.25],
            [2.00, 4.25],
            [1.75, 4.25],
            [1.50, 4.25],
            [1.25, 4.25], 
            [1.00, 4.25], 
            [0.75, 4.25], #(bas gauche) 
            [0.75, 4.00],
            [0.75, 3.75],
            [0.75, 3.50],
            [0.75, 3.25],
            [0.75, 3.00],
            [0.75, 2.75],
            [0.75, 2.50],
            [0.75, 2.25],
            [0.75, 2.00],
            [0.75, 1.75], # (haut gauche)
            [1.00, 1.75],
            [1.25, 1.75],
            [1.50, 1.75],
            [1.75, 1.75], # (stop)
            [2.00, 1.75],
            [2.25, 1.75]]

    position = 0
    while True:
        try:
            x = listePosition[position][0]
            y = listePosition[position][1]
        except IndexError:
            position = 0
        try:
            carALiot.update_doc({
                "/doc/voiture": [{
                    "x": x,
                    "y": y,
                    "id": 1,
                    "a": x,
                    "d": y,
                    "speed": 0,
                    "linkStream": linkStream,
                }]
            })
            sleep(0.75)
            position+=1
            if position == 23:
                sleep(1)
        except KeyboardInterrupt:
            break


carALiot.on_start(callback=start)
carALiot.run()
