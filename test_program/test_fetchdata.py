import pymysql
import json
def handle_request(conn,json_str,day,time):
    db = pymysql.connect("172.17.118.89", "root", "123456", "pycom")
    cursor = db.cursor()
    cursor = db.cursor()
    sql = """select * from console_device"""
    reply = {"Messagetype":'result'}
    deviceList = []
    gatewayId = json_str['GatewayID']
    reply["GatewayID"] = gatewayId
    reply["Day"] = day
    reply["Time"] = time

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            deviceList.append(row[1])

        # return deviceList
    except:
        print('No the table')

    reply["DeviceList"] = deviceList
    reply_str = json.dumps(reply)
    conn.send(bytes(reply_str,'utf8'))
    conn.close()



