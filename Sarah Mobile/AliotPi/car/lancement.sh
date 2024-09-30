#!/bin/bash


cd Aliot-car
source ./venv/bin/activate
cd car/
python stream.py &
python blinky.py &
aliot run car 
