import paho.mqtt.client as mqtt
import time

class AppMqtt:
	def __init__(self,username,password,host,port,topicList,onMessage=None):
		mqtt_username = username 
		mqtt_password = password
		self.on_message = self.on_message_func
		self.topicList = topicList
		
		if onMessage != None:
			self.on_message = onMessage
 
		self.mqttClient = mqtt.Client()
		while True:
			try:
				print('mqtt Connecting...')
				self.mqttClient.username_pw_set(mqtt_username, mqtt_password)  
				self.mqttClient.connect(host, port, 60)
				break
			except:
				print ("in mqtt except")
			time.sleep(5)
				
		self.setHandle(self.on_message,self.on_connect)

	def send(self,topic,sendContent,Qos):
		try:
			self.mqttClient.publish(topic,sendContent,qos=Qos)
		except:
			print ("mqtt error")
	
			
	def setHandle(self,onMessageHandle,onConnectHandle):
		self.mqttClient.on_message=onMessageHandle
		self.mqttClient.on_connect = onConnectHandle

	
	def on_message_func(self,client, userdata, message):
		print("message received " ,message.payload)
		print("message topic=",message.topic)
		print("message qos=",message.qos)
		print("message retain flag=",message.retain)
		
		
	def on_connect(self_AppMqtt,self_mqtt, client, userdata, rc):
		print(self_AppMqtt,self_mqtt, client, userdata, rc)
		if rc==0:
			print("Connected with result code "+str(rc))
			self_mqtt.subscribe(self_AppMqtt.topicList)
		else:
			print("Connection failed")
			
	def loop_forever(self):
		self.mqttClient.loop_forever()
		
	def loop_start(self):
		self.mqttClient.loop_start()