#
# Simple Tick Data Server with ZeroMQ
#
import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:5555')

AAPL = 100.

while True:
    AAPL += random.gauss(0, 1) * 0.5
    msg = 'AAPL %.4f' % AAPL
    socket.send_string(msg)
    print(msg)
    time.sleep(random.random() * 2)
