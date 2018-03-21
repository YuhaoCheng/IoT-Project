import time
def getDay():
    print('the day!!')
    day = time.strftime('%Y-%m-%d',time.localtime())
    return day

def getTime():
    print('the time!')
    real_time =time.strftime('%H:%M:%S', time.localtime())
    return real_time

if __name__=='__main__':
    temp = getTime()
    day = getDay()
    print('the day is %s'%day)
    print('the time is %s'%temp)