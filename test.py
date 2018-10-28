from lib import *

def printdata(client, userdata, message):
	print("received from server:")
	print(message.payload)

def randomSensor():
	keys = ['signature', 'temperature', 'humidity', 'waterlevel', 'pH', 'turbidity', 'status', 'timestamp']
	sensor = {}
	for k in keys:
		sensor[k] = random.randint(1,50)

	return sensor

def randomActuator():
	keys = ['signature', 'pump', 'fan', 'light', 'timestamp']
	actuator = {}
	for k in keys:
		actuator[k] = random.randint(0,1)

	return actuator

def testSend(count):
	device = AWSInterface()
	device.receiveData("dev_f2a682bc2da14f5bb7043ce5d18faa7f/task",printdata)

	while True:
		# data = {}
		# data['sensor']=randomSensor()
		# data['actuator']=randomActuator()
		# device.sendData(data)
		# print("sending..")
		# time.sleep(2)
		# count-=1
		print("waiting for server...")
		time.sleep(10)

# fp = open('device_list.txt','r');
# devices = fp.readlines()
# fp.close()
# devices = [x.strip() for x in devices]
devices = ["dev_f2a682bc2da14f5bb7043ce5d18faa7f"]

for device in devices:
	parser =SafeConfigParser()
	parser.read("device.conf")
	parser['device']['clientId'] = device
	parser['device']['privateKeyPath'] = "../keys/"+device+"_private.key"
	parser['device']['certificatePath'] = "../keys/"+device+"_cert.pem"
	device = device.split('_')
	parser['device']['userId'] = "usr_"+device[1]
	with open('device.conf','w') as configfile:
		parser.write(configfile)

	testSend(5)