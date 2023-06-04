from microbit import *
from ultrasonic import Ultrasonic
import radio
radio.config(group=21)
radio.on()
ultrasonic_sensor = Ultrasonic()
while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    if distance_value < 50 :
        # s = 0
        radio.send('1')
        #radio.send(str(int(s)))

        
    
