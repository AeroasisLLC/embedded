# # importing the requests library 
import requests
import uuid
import json
  
# # api-endpoint
for i in range(1):
	user_id = "usr_"+(uuid.uuid4().hex)
	

	URL = "https://n8u32bu2v8.execute-api.us-west-2.amazonaws.com/beta/init-setup"
	  
	  
	# # defining a params dict for the parameters to be sent to the API 
	PARAMS = { 'user_id':user_id,
			   'device_type':"aeroasis_device"
				} 
	  
	# # sending get request and saving the response as response object 
	r = requests.get(url = URL,params = PARAMS) 

	# # extracting data in json format 
	data = r.json()
	print(json.dumps(data,indent=4))

	#print(data)

	cert=data['body']['certificate']
	priv=data['body']['privateKey']
	device_name = data['body']['thingName']
	
	dev_list = open("E:/aeroasis/Embedded/device_list.txt",'a')
	dev_list.write(device_name)
	dev_list.write('\n')
	dev_list.close()

	fn_c=open("E:/aeroasis/keys/"+device_name+"_cert.pem",'x')
	fn_c.write(cert)
	fn_c.close()


	fn_p=open("E:/aeroasis/keys/"+device_name+"_private.key",'x')
	fn_p.write(priv)
	fn_p.close()



