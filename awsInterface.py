from lib import *

class AWSInterface():

	parser = SafeConfigParser()
	parser.read('device.conf')
	host = parser.get('device','host')
	port = int(parser.get('device','port'))
	clientId = parser.get('device','clientId')
	topic = parser.get('device','topic')
	rootCAPath = parser.get('device','rootCAPath')
	privateKeyPath = parser.get('device','privateKeyPath')
	certificatePath = parser.get('device','certificatePath')


	def __init__(self):
		self.myAWSIoTMQTTClient = AWSIoTMQTTClient(AWSInterface.clientId)
		self.myAWSIoTMQTTClient.configureEndpoint(AWSInterface.host, AWSInterface.port)
		self.myAWSIoTMQTTClient.configureCredentials(AWSInterface.rootCAPath, AWSInterface.privateKeyPath, AWSInterface.certificatePath)
		self.myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
		self.myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
		self.myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
		self.myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
		self.myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
		if(self.myAWSIoTMQTTClient.connect()):
			print("Connected successfully")
		else:
			print("Not Connected")

	def receiveData(self,topic,func):
		self.myAWSIoTMQTTClient.subscribe(topic,1,func)

	def sendData(self,data):
		self.myAWSIoTMQTTClient.publish(AWSInterface.topic, data, 1)