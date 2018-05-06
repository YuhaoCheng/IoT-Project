# Web Application 

## Note
* Before deploying the Web Application, you need to follow the instructions on [Django](https://www.djangoproject.com/) to install Django
* [webMonitor](https://github.com/YuhaoCheng/IoT-Project/tree/master/webapp/webMonitor) is a Java project which is dicarded. However, I'm gload that you can complete it if you are familiar with Java web developing.
* You also need to install the [MySQL](https://www.mysql.com/) in your server

## Usage
1. Download [web](https://github.com/YuhaoCheng/IoT-Project/tree/master/webapp/web) in `$HOME/web`
2. `cd $HOME/web`
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py runserver 0.0.0.0:8000`