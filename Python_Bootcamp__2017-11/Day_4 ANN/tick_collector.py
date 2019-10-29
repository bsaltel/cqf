#
# Simple Tick Data Collector with ZeroMQ & pandas
#
import zmq
import datetime
import pandas as pd

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5555')

socket.setsockopt_string(zmq.SUBSCRIBE, 'AAPL')

raw = pd.DataFrame()

i = 0
while True:
    msg = socket.recv_string()
    i += 1
    t = datetime.datetime.now()
    print('%s | ' % str(t), msg)
    sym, value = msg.split()
    raw = raw.append(pd.DataFrame({sym: float(value)}, index=[t]))
    resam = raw.resample('5s', label='right').last()
    if i % 10 == 0:
        print('\n', resam.tail(3), '\n')
