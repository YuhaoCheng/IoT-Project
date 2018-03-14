PATH='./1.txt'
import numpy as np
import pandas
# import matplotlib as mpl
# mpl.use('Agg')
import matplotlib.pyplot as plt
def read_data():
    file = open(PATH, 'r')
    whole_data = []
    #data = []
    for line in file:
        words = line.split(',')
        data = []
        for word in words:
            if word == '\n':
                continue
            data.append(int(word))
        whole_data.append(data)

    array = np.array(whole_data)
    return array
    print(array)

def draw_figure(data):
    print('the function of draw the figure')
    print(data.shape)
    number = data.size / 3
    temperature_data = data[:,0]
    humidity_data = data[:,1]
    light_data = data[:,2]
    time = np.arange(0,5*number,5)
    print(temperature_data)
    print(humidity_data)
    print(light_data)
    # plt.plot(time,temperature_data,'r--',time,humidity_data,'b-',time,light_data,'g.-')
    plt.figure(1)
    plt.plot(time,temperature_data,'r--')
    plt.xlabel('Time/s')
    plt.ylabel('Temperature/t')
    plt.savefig('Temperature-Time.jpg')
    plt.figure(2)
    plt.plot(time,humidity_data,'b-')
    plt.xlabel('Time/s')
    plt.ylabel('Humidity/%')
    plt.savefig('Humidity-Time.jpg')
    plt.figure(3)
    plt.plot(time,light_data,'g.-')
    plt.xlabel('Time/s')
    plt.ylabel('Light/lux')
    plt.savefig('Light-Time.jpg')
    plt.show()



if __name__ == '__main__':
    data = read_data()
    # str = "123\n1"
    # str.strip('\n')
    # print(str)
    draw_figure(data)
    print('the main function of the program')
