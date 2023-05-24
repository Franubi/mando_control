from microbit import *
import radio
from Maqueen import Maqueen

mq = Maqueen()

radio.on()
radio.config(channel=10, group=0)

while True:
    message = radio.receive()
    if message == 'left':
        mq.motor_stop_all()
        sleep(500)  
        mq.stop()
    elif message == 'right':
        mq.turn_right()
        sleep(500)  
        mq.stop()
    elif message == 'forward':
        mq.forward()
        sleep(500)  
        mq.stop()
    sleep(100)
