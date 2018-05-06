# IoT-Project
This is my final year project of university<br/>
## How to send the messgae to the Alibaba cloud server
1. Create a ECS by using your account
2. Get the public and private IP address of the ECS
3. Upload the file in ./server/socket_server.py to your server
4. Change the IP address in socket_server.py to **private address** of your own ECS  
5. Upload the file in ./pycom to your boards and start the boards

## The usage of the project

1. The [pycom](https://github.com/YuhaoCheng/IoT-Project/tree/master/pycom) is the files you need yo download to your LoPy boards.
2. The [server](https://github.com/YuhaoCheng/IoT-Project/tree/master/server) is the files you need to deploy in your Alibaba.
3. The [webapp](https://github.com/YuhaoCheng/IoT-Project/tree/master/webapp) is the Web Application in the project. Your need to follow the instruction on [Django](https://www.djangoproject.com/) to install the Django service on your server and deply the Web Application.
4. The [test_program](https://github.com/YuhaoCheng/IoT-Project/tree/master/test_program) is tool to help you to debug the program in your Server.

## Note
* The [Console](https://github.com/YuhaoCheng/IoT-Project/tree/master/webapp/Console) and [webMonitor](https://github.com/YuhaoCheng/IoT-Project/tree/master/webapp/webMonitor) are discarded. However, if you are familiar with Java, I'm appreciated that you can imporve these web project. 
