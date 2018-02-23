import socket
if __name__ == '__main__':
    ip_port = ('127.0.0.1',8080)
    web = socket.socket()
    web.bind(ip_port)
    web.listen(5)
    print('waiting....')
    #databuf = {}
    #location = []
    #data = []
    while True:
        conn, addr = web.accept()
        data = conn.recv(1024)
        result = str(data,encoding='utf8')
        results = result.split(':')
        results.remove('')
        print(results)
        for line in results:
            item = line.split(',')
            name = item[0] + '.txt'
            with open(name,'a+') as f:
                f.write(item[1] + ',')
                f.write(item[2] + ',')
                f.write(item[3] + ',')
                f.write('\n')

        #print(data)
        print(result)
        conn.send(bytes('<h1>welcome to socket server</h1>', 'utf8'))
        conn.close()
