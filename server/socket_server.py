import socket
import json
import threading
import pymysql
import sys
sys.path.append(".")
import node_time
def handle_receive(conn):
    data = conn.recv(1024)
    result = str(data, encoding='utf8')
    print(result,type(result))   # the type of result is String
    print('-------------------------')
    json_str = json.loads(result)
    print(json_str,type(json_str))  # the type of json_str is dict
    conn.send(bytes('ACK', 'utf8'))
    # data_dict = json.dumps(json_str)
    data_dict = json_str
    temp_time = node_time.getTime()
    temp_day = node_time.getDay()
    data_dict['Day'] = temp_day
    data_dict['Time'] = temp_time
    # db = pymysql.connect("localhost","root","123456","")
    # with open('data.json','a') as f:
    #     json.dump(json_str,f)
    database_handler = threading.Thread(target=database_handle, args=(data_dict,))
    database_handler.start()
    print(data_dict)
    conn.close()

def database_handle(data):
    db = pymysql.connect("172.17.118.89", "root", "123456", "pycom")
    cursor = db.cursor()
    if data['Messagetype'] == 'data':
        deviceID = data['DeviceID']
        temperature = data['Temperature']
        humidity = data['Humidity']
        light = data['Light']
        day = data['Day']
        time = data['Time']
        sql = """insert into console_data(deviceID,temperature,humidity,light,time,day) values('%s','%d','%d','%d','%s','%s')""" % (deviceID,temperature,humidity,light,time,day)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        #db.close()

    if data['Messagetype'] =='warning':
        message = data['Message']
        attribute = data['attribute']
        deviceID = data['DeviceID']
        day = data['Day']
        time = data['Time']
        sql = """insert into console_warning(time,day,attribute,message,deviceID) values('%s','%s','%s','%s','%s')""" % (time, day, attribute, message, deviceID)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        #db.close()
    db.close()


if __name__ == '__main__':
    ip_port = ('172.17.118.89',8090)
    web = socket.socket()
    web.bind(ip_port)
    web.listen(5)
    print('waiting....')
    #databuf = {}
    #location = []
    #data = []
    while True:
        conn, addr = web.accept()
        # results = result.split(':')
        # results.remove('')
        # print(results)
        # for line in results:
        #     item = line.split(',')
        #     name = item[0] + '.txt'
        #     with open(name,'a+') as f:
        #         f.write(item[1] + ',')
        #         f.write(item[2] + ',')
        #         f.write(item[3] + ',')
        #         f.write('\n')

        #print(data)
        #print(result)
        client_handler = threading.Thread(target=handle_receive,args=(conn,))
        client_handler.start()