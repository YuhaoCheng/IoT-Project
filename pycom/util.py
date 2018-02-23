import socket
from network import LoRa
def sendData(data, way='WIFI', ip='127.0.0.1'):
    temp = ""
    keys = data.keys()
    for key in keys:
        line = data.get(key)
        temp = temp + key
        for item in line:
            temp = temp + ',' + str(item)
        temp = temp + ':'
    print(temp)
    if way=='WIFI':
        print('send the data using WiFi')
        ip_port = (ip, 8080)
        web = socket.socket()
        web.connect(ip_port)
        web.sendall(bytes(temp, 'utf8'))
        server_reply = web.recv(1024)
        print(str(server_reply, 'utf8'))
        web.close()
    if way=='LORA':
        print('send the data use LoRa')
        lora = LoRa(mode=LoRa.LORA)
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        s.setblocking(False)
        s.send(data)
        s.close()
def sendWarning(type,way='WIFI',ip='127.0.0.1'):
    message = 'Error in sending the Warning message'
    if type == 1:
        message = 'Temperature is changed so large'
    if type == 2:
        message = 'Humidity is changed so large'
    if type == 3:
        message = 'Light is changed so large'

    if way == 'WIFI':
        print('send the warning message using WiFi')
        ip_port = (ip, 8080)
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

if __name__ == '__main__':
    databuf = [10,20,30]
    databuf2 = [11,21,31]
    buf = {'1':databuf, '2':databuf2}
    sendData(buf)
