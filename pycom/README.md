# The programs in LoPy developing boards

## Note
* The developing process of the project is based on the [Atom editor](https://atom.io/).
* The method to download the files into your boards is on [Pycom Documnetation](https://docs.pycom.io/).
* The method reading  the data from DHT is from [DHT_PyCom](https://github.com/JurassicPork/DHT_PyCom).
* The method reading  the data from BH1750FVI is from [Pycom Document I2C](https://docs.pycom.io/chapter/tutorials/all/i2c.html)

## Usage
1. [gateway](https://github.com/YuhaoCheng/IoT-Project/tree/master/pycom/gateway) needs to be deployed in your Gateway node
2. [node](https://github.com/YuhaoCheng/IoT-Project/tree/master/pycom/node) needs to be deployed in your End-device node
3. You need to modify the `configuration.py`
4. You need to modify the `address` attribute in `pymakr.conf` to make sure that you can successfully deploy the project in your LoPy boards 