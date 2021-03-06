import socket
import json
from network import LoRa
from machine import SD
import os
def sendData(data, way='WIFI', ip='127.0.0.1'):
    temp = json.dumps(data)
    print(temp)
    if way=='WIFI':
        print('send the data using WiFi')
        ip_port = (ip, 8090)
        web = socket.socket()
        web.connect(ip_port)
        web.sendall(bytes(temp, 'utf8'))
        server_reply = web.recv(1024)
        reply_str = server_reply.decode('utf8')
        print('The reply from server: ', reply_str)
        web.close()
        return reply_str
    if way=='LORA':
        print('send the data use LoRa')
        lora = LoRa(mode=LoRa.LORA, region=LoRa.AS923)
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        s.setblocking(False)
        s.send(data)
        recv_data = s.recv(64)
        print(recv_data)
        s.close()
def sendWarning(type,way='WIFI',ip='127.0.0.1'):
    message = 'Error in sending the Warning message'
    if type == 1:
        message = '{"DeviceID":"1","Messagetype":"warning","attribute":"Temperature","Message":"Temperature is changed so large"}'
    if type == 2:
        message = '{"DeviceID":"1","Messagetype":"warning","attribute":"Humidity","Message":"Humidity is changed so large"}'
    if type == 3:
        message = '{"DeviceID":"1","Messagetype":"warning","attribute":"Light","Message":"Light is changed so large"}'

    if way == 'WIFI':
        print('send the warning message using WiFi')
        ip_port = (ip, 8090)
        web = socket.socket()
        web.connect(ip_port)
        web.sendall(bytes(message, 'utf8'))
        server_reply = web.recv(1024)
        print(str(server_reply, 'utf8'))
        web.close()

    if way == 'LORA':
        print('send the data use LoRa')
        lora = LoRa(mode=LoRa.LORA)
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        s.setblocking(False)
        s.send(message)
        s.close()

def storeData(data):
    sd = SD()
    os.mount(sd, '/sd')
    # check the content
    os.listdir('/sd')
    print(data)
    print('This is the sore data method')

def sendRequest(data, ip='127.0.0.1', port=8090):
    # device_list =[]
    temp = json.dumps(data)
    ip_port = (ip,port)
    web = socket.socket()
    web.connect(ip_port)
    web.sendall(bytes(temp, 'utf8'))
    server_reply = web.recv(1024)

    return server_reply

def sendLoraData(data):
    lora = LoRa(mode=LoRa.LORA, rx_iq=True)
    lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    lora_sock.setblocking(False)
    lora_sock.send(data)
    while True:
        if lora_sock.recv(128) == b'ACK':
            return True
def recviceLoraData():
    lora = LoRa(mode=LoRa.LORA, rx_iq=True)
    lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    lora_sock.setblocking(False)
    while True:
        data = lora_sock.recv(128)
        if data != '':
            lora_sock.send('ACK')
            return data


if __name__ == '__main__':
    databuf = [10,20,30]
    databuf2 = [11,21,31]
    buf = {'1':databuf, '2':databuf2}
    sendData(buf)
