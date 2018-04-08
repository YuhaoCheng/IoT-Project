"""
Funtion of the node:
    1. send the data to the server, the data is not a single one, it consists of many items of data
    2. receive the data from other nodes
    3. save the other devices' data into the SD card
    4. Control the devices in it's area: if some device isn't registered in the Cloud, it can't re-send it's data to the server. Or directly block it.

Original Data format:
    1. Data: {'Messagetype':'data','DeviceID':'1','Temperature':0, 'Humidity':0, 'Light':0}
    2.Warning Message: '{"DeviceID":"1","Messagetype":"warning","attribute":"Temperature","Message":"Temperature is changed so large"}'

Work Flow:
    1. Request the devices list from the cloud server:
        a. Send the GatewayID to the server by socket: {"GatewayID":"1", "Messagetype":"request"} by socket through Wi-Fi
        b. Receive the device list:
            {"GatewayID":"1", "Messagetype":"result", "DevicesList":["1","2","3"],"DateTime":"2018-3-30_12:30:54"}
    2. Deal with the message from other nodes
        a. If the device is not in the list, it will not re-transmit the data
        b. When the gateway counts 20 results from other nodes, it will store the data into the SD card named by 2018-3-30_12:30:54-01
        c. Send the ACK message to the node, if it successfully re-transmit the data
        d. It will send the NODEVICE message to the node, if the device isn't registered in the server(The LED will change to RED all the time, the node)
        e. It will send the ERROR message to the node, if the message isn't successfully sent to server(The LED will change to BLUE all the time, the node)


"""

# import json
# # import threading
# import _thread
# import socket
# import util
# import time
# from network import LoRa
#
# def handle_save(buf, file_name):
#     print("The method to save the data")
#
#
#
# if __name__=='__main__':
#     print('This is the gateway node!')
#     # lora = LoRa(mode=LoRa.LORA, rx_iq=True)
#     COUNT = 0 # To record the number of the message
#     buf = {} # To record the data temporally
#     sn = 1 # To count the file
#     request = '{"GatewayID":"1","Messagetype":"request"}' # the request to the server
#     # result = util.sendRequest()
#
#     lora = LoRa(mode=LoRa.LORA)
#     lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#     lora_sock.setblocking(False)
#
#
#     # result_dict = json.dumps(result)
#     # date_time = result_dict['DateTime'] # Get the time from the server
#     # device_list = result_dict['DeviceList'] # Get the device list from the server
#
#     # node_handler = threading.Thread(target=handle_lora_reveive(), args=(device_list, date_time,))
#     # node_handler.start()
#
#     while True:
#         data = lora_sock.recv(64)
#         time.sleep(5)
#         # util.storeData(data)
#         print(data)
#
#     #     COUNT = COUNT + 1
#     #     recv_pkg = lora_sock.recv(1024)
#     #
#     #
#     #     if COUNT==9:
#     #         file_name = str(date_time,sn)
#     #         sn = sn + 1
#     #         save_handler = threading.Thread(target=handle_save(), args=(buf, file_name,))
#     #         save_handler.start()
#     #
from network import LoRa
import socket
import time
import util
import json
import _thread
import configuration as CONFIG

# global deviceList

def getDeviceList():
    request = {"GatewayID":CONFIG.GATEWAYID,"Messagetype":'request'}
    reply_str = util.sendData(request,'WIFI',CONFIG.SERVER_ADDR)
    reply_json_obj = json.loads(reply_str)
    deviceList = reply_json_obj['DeviceList']
    # global deviceList=['1',]
    # deviceList = ['1','3']
    return deviceList

def handle_transmit(data):
    util.sendData(data,'WIFI', CONFIG.SERVER_ADDR)
    print('Re-transmit the data to server')

if __name__=='__main__':
    deviceList = getDeviceList()
    print('The device List from the database:')
    print(deviceList)

    while True:
        check_flag=False
        # Create the lora socket
        lora = LoRa(mode=LoRa.LORA, region=LoRa.AS923)
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        s.setblocking(True)
        # receive the data
        data = s.recv(1024)
        print('Recv the data', data, type(data))
        data_str = data.decode('utf8')
        print('The data string', data_str, type(data_str))
        json_obj = json.loads(data_str)
        print('The json is', json_obj,type(json_obj))
        print(json_obj['Messagetype'])
        for device in deviceList:
            if json_obj['DeviceID']==device:
                _thread.start_new_thread(handle_transmit,(json_obj,))
                s.send('ACK')
                check_flag = True

        if (not check_flag):
            print('Not transmit the data')
            s.send('NO')
    # time.sleep(5)
