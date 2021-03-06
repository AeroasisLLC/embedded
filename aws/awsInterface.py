import sys
sys.path.insert(0, '../lib')
from lib import *

class AWSInterface():

    def __init__(self):
        parser = SafeConfigParser()
        parser.read('../config_files/device.conf')
        self.host = parser.get('device', 'host')
        self.port = int(parser.get('device', 'port'))
        self.clientId = parser.get('device', 'clientId')
        self.userId = parser.get('device', 'userId')
        self.topic = parser.get('device', 'topic')
        self.rootCAPath = parser.get('device', 'rootCAPath')
        self.privateKeyPath = parser.get('device', 'privateKeyPath')
        self.certificatePath = parser.get('device', 'certificatePath')
        self.growId = parser.get('grow', 'growId')
        parser.read('../config_files/plant.conf')
        self.growStartDate = parser.get('PlantInfo', 'plantingDate')
        self.growStartDate = strtoDate(self.growStartDate)
        self.myAWSIoTMQTTClient = AWSIoTMQTTClient(self.clientId)
        self.myAWSIoTMQTTClient.configureEndpoint(self.host, self.port)
        self.myAWSIoTMQTTClient.configureCredentials(
            self.rootCAPath, self.privateKeyPath, self.certificatePath)
        self.myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        # Infinite offline Publish queueing
        self.myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)
        self.myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myAWSIoTMQTTClient.configureConnectDisconnectTimeout(20)  # 10 sec
        self.myAWSIoTMQTTClient.configureMQTTOperationTimeout(20)  # 5 sec
        while True:
            
            try:
                self.logger.debug('Trying to connect to aws..')
                self.myAWSIoTMQTTClient.connect()
            except Exception as e:
                self.logger.warning('Not connected to aws..')
                self.logger.warning(e)
                print(e)
                print("Not connected...")
                print("retrying in 5 seconds....")
                time.sleep(5)
                continue
            else:
                self.logger.debug('connected to aws..')
                print("connected...")
                break
        
        

    def receiveData(self, topic, func):
        self.logger.debug('subscribed to topic -- %s, activated callback function %s',topic,func)
        self.myAWSIoTMQTTClient.subscribe(topic, 1, func)

    def sendData(self, data):
        packet = self.makePacket(data)
        try:
            self.logger.debug('Trying to send data to aws..')
            self.myAWSIoTMQTTClient.publish(self.topic, packet, 1)
        except Exception as e:
            self.logger.warning('packet send to aws failed..')
            self.logger.warning(e)
            self.logger.debug('packet sending into queue here after')
            print(e)
            print("packet sending failed...")
            print("packet sending into queue here after....")

        else:
            self.logger.debug('packet sent to aws sucessfull')
            print("packet sent successfully...")

       

    def makePacket(self, data):
        packet = {}
        packet['device_id'] = self.clientId
        packet['user_id'] = self.userId
        packet['time_stamp'] = str(datetime.datetime.now())
        packet['sensor_data'] = data['sensor']
        packet['grow_id'] = self.growId
        packet['time_from_start'] = str(datetime.date.today()-self.growStartDate)
        packet['actuator_data'] = data['actuator']
        iotPacket = json.dumps(packet)
        return iotPacket

    def sendCameraData(self, data):
        response = requests.post("https://aws.savetos3_api", data=data)
        return response
