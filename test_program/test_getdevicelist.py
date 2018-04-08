import json
import socket

if __name__=='__main__':
    ip_port = ('59.110.241.225',8090)
    web = socket.socket()
    web.connect(ip_port)
    temp = {"GatewayID":'1',"Messagetype":'request'}
    temp_str = json.dumps(temp)
    web.sendall(bytes(temp_str,'utf8'))
    print('Send the data')
    recv_bytes = web.recv(1024)
    data = str(recv_bytes,encoding='utf8')
    print(data)