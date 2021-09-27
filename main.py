# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import DeconZ
from mqtt import AppMqtt
from ConfigFile import readConfigFile

CONFIG_FILE = "/boot/tradfri.json"

class MqttService:
    def __init__(self,config=None):
        self.mqtt_username="tradfri_host"
        self.mqtt_password = "q4k9m5w6"
        self.mqtt_host = "tailor.cloudmqtt.com"
        self.mqtt_port = 13357
        self.mqtt_topicList = [('//',0)]
        self.mqtt_send_topic = "tradfri"
        self.mqtt_send_Qos = 0

        if config!= None:
            self.__load_condif_file(config)

        self.mqtt = AppMqtt(username=self.mqtt_username,
                            password=self.mqtt_password,
                            host=self.mqtt_host,
                            port=self.mqtt_port,
                            topicList=self.mqtt_topicList)
        self.mqtt.loop_start()

    def __load_condif_file(self,config):
        self.mqtt_username = config['mqtt_username']
        self.mqtt_password = config['mqtt_password']
        self.mqtt_host = config['mqtt_host']
        self.mqtt_port = config['mqtt_port']
        self.mqtt_send_topic = config['mqtt_send_topic']
        self.mqtt_send_Qos = config['mqtt_send_Qos']


    def publish(self, content):
        self.mqtt.send(self.mqtt_send_topic, content, self.mqtt_send_Qos);

class DeconZService:
    def __init__(self,config=None):
        self.sleep_time = 5

        if config != None:
            self.__load_condif_file(config)

    def __load_condif_file(self,config):
        self.sleep_time = config['sleep_time']

    def query(self):
        return DeconZ.query()



import time


def run1():
    #1. read config parameters to init mqttServer
    configParams = readConfigFile(CONFIG_FILE)
    mqttServer = MqttService(configParams)
    deconZService = DeconZService(configParams)

    while True:
        sensorValues = deconZService.query()
        for sensorValue in sensorValues:
            mqttServer.publish(sensorValue.toJson())
        time.sleep(deconZService.sleep_time)


if __name__ == '__main__':
    run1()

