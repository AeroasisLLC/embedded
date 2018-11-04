# # importing the requests library
import requests
import uuid

# # api-endpoint

user_id = "usr_"+(uuid.uuid4().hex)
URL = "https://n8u32bu2v8.execute-api.us-west-2.amazonaws.com/beta/create-new-device"

# # defining a params dict for the parameters to be sent to the API
PARAMS = { 	'user_id':user_id,
			'device_type':"aeroasis_device"
				}

# # sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# # extracting data in json format
data = r.json()
print(data)

# print(data)

cert = data['body']['certificate']
priv = data['body']['privateKey']
device_name = data['body']['device_id']

fn_c = open("../keys/"+device_name+"_cert.pem", 'x')
fn_c.write(cert)
fn_c.close()

fn_p = open("../keys/"+device_name+"_private.key", 'x')
fn_p.write(priv)
fn_p.close()
