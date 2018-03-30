"""
Funtion of the node:
    1. send the data to the server
    2. receive the data from other nodes
    3. get the data in its location
"""
import bh1750fvi as fvi
import time
import util
import configuration as CONFIG
from dth import DTH
from machine import I2C
global temperature
global humidity
global light

def readTH(pin):
    global temperature
    global humidity
    th = DTH(pin, 0)
    result = th.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity

def readLight():
    global light
    i2c = I2C(0, I2C.MASTER, baudrate=100000)
    light_sensor = fvi.BH1750FVI(i2c)
    light = light_sensor.read()

def sendData(data, way='WIFI', ip='59.110.241.225'):
    # convert the list to string and send to the WiFi node(use the LoRa) or
    # the server(use the WiFi)
    HAVE_FLAG = 0
    if data:
        print('Not empty')
        HAVE_FLAG = 1
    else:
        print()
        EMPTY_FLAG = 0
        return 0
    #convert the data list to string

    #when HAVE_FLAG=1 judge the way and send the data

if __name__ == '__main__':
    global temperature
    global humidity
    global light
    # databuf = [0,0,0]  # if server receives [0,0,0], meaning that the program not works well
    # buf = {'1': databuf}  # in this prototype, we assume the location sequence number is 1
                          # and we also assume that we just send one data
    buf = {'Messagetype':'data','DeviceID':'1','Temperature':0, 'Humidity':0, 'Light':0} # use the dict to store the whole data
    changebuf = [0,0,0]
    changes = [0,0,0]
    a = 0 # jude whether it is the first time to transmit the data
    SEND_MSG_FLAG=0 # 1 means that the change is large enough to send the data or it meets some situation to send the data
    COMM_MODE = 'WIFI' # in this prototype we assume that the communication mode is WIFI
    while True:
        i =0 # index of the changes[]
        readTH('G14')
        readLight()
        # databuf[0]= temperature
        # databuf[1] = humidity
        # databuf[2] = light
        buf['Temperature'] = temperature
        buf['Humidity'] = humidity
        buf['Light'] = light
        util.sendData(buf,COMM_MODE,CONFIG.SERVER_ADDR)
        print('successfully send the data')
        time.sleep(5)
        if a:
            print('judege the change from the second data transmit')
            changes[0] = abs(temperature-changebuf[0])
            changes[1] = abs(humidity-changebuf[1])
            changes[2] = abs(light-changebuf[2])
            print('the value of changes is: ' + str(changes[0]) +','+ str(changes[1]) +','+ str(changes[2]))

            if changes[0] >= 1:
                print('temperature changes')
                util.sendWarning(1, COMM_MODE,CONFIG.SERVER_ADDR)
                print('Successful send the Warning Message')

            if changes[1] >= 1:
                print('humidity changes')
                util.sendWarning(2, COMM_MODE,CONFIG.SERVER_ADDR)
                print('Successful send the Warning Message')
            if changes[2] > 10:
                print('light changes')
                util.sendWarning(3, COMM_MODE,CONFIG.SERVER_ADDR)
                print('Successful send the Warning Message')

            """
            for change in changes:
                if i==0:
                    if change>1:
                        #databuf[i] = temperature
                        #SEND_MSG_FLAG = 1
                        i = i + 1
                        print('temperature change')
                        #type = 1
                        util.sendWarning(1, COMM_MODE, '59.110.241.225')
                        print('Successful send the Warning Message')
                if i==1:
                    if change>1:
                        #databuf[i] = humidity
                        #SEND_MSG_FLAG = 1
                        i = i + 1
                        print('humidity change')
                        #type = 2
                        util.sendWarning(2, COMM_MODE, '59.110.241.225')
                        print('Successful send the Warning Message')
                if i==2:
                    if change>10:
                        #databuf[i] = light
                        #SEND_MSG_FLAG = 1
                        i = i + 1
                        #type = 3
                        print('light change')
                        util.sendWarning(3, COMM_MODE, '59.110.241.225')
                        print('Successful send the Warning Message')
            """
            changebuf[0] = temperature
            changebuf[1] = humidity
            changebuf[2] = light
            """
            if SEND_MSG_FLAG:
                util.sendWarning(type, COMM_MODE, '59.110.241.225')
                print('Successful send the Warning Message')
            """
        else:
            changebuf[0] = temperature
            changebuf[1] = humidity
            changebuf[2] = light
            a = 1
        print('the value of changebuf is' + str(changebuf[0]) +','+ str(changebuf[1]) +','+ str(changebuf[2]) +','+ '\n')
    # if the server receive
