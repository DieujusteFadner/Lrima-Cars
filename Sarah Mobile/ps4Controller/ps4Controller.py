from pyPS4Controller.controller import Controller
from car import Car

'''

on_x_press
on_x_release
on_triangle_press
on_triangle_release
on_circle_press
on_circle_release
on_square_press
on_square_release
on_L1_press
on_L1_release
on_L2_press
on_L2_release
on_R1_press
on_R1_release
on_R2_press
on_R2_release
on_up_arrow_press
on_up_down_arrow_release
on_down_arrow_press
on_left_arrow_press
on_left_right_arrow_release
on_right_arrow_press
on_L3_up
on_L3_down
on_L3_left
on_L3_right
on_L3_x_at_rest  # L3 joystick is at rest after the joystick was moved and let go off on x axis
on_L3_y_at_rest  # L3 joystick is at rest after the joystick was moved and let go off on y axis
on_L3_press  # L3 joystick is clicked. This event is only detected when connecting without ds4drv
on_L3_release  # L3 joystick is released after the click. This event is only detected when connecting without ds4drv
on_R3_up
on_R3_down
on_R3_left
on_R3_right
on_R3_x_at_rest  # R3 joystick is at rest after the joystick was moved and let go off on x axis
on_R3_y_at_rest  # R3 joystick is at rest after the joystick was moved and let go off on y axis
on_R3_press  # R3 joystick is clicked. This event is only detected when connecting without ds4drv
on_R3_release  # R3 joystick is released after the click. This event is only detected when connecting without ds4drv
on_options_press
on_options_release
on_share_press  # this event is only detected when connecting without ds4drv
on_share_release  # this event is only detected when connecting without ds4drv
on_playstation_button_press  # this event is only detected when connecting without ds4drv
on_playstation_button_release  # this event is only detected when connecting without ds4drv

'''
car = Car()

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       
       car.lightsOn()
       
    def on_square_press(self):
        
        car.lightsOff()
       
    def on_L3_right(self, value):
    
        car.turnRight()
       	print(value) 
        
    def on_L3_left(self, value):
        print(value)
        car.turnLeft()
        
    def on_L3_x_at_rest(self):
        
        car.centerWheel()
    
    def on_R2_press(self, value):
        
        car.forward()
        print(value)

    def on_R2_release(self):
        
        car.stop()
        
    def on_L2_press(self, value):
        car.backward()

    def on_L2_release(self):
        car.stop()
        
    
    
    
    
        
    

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
