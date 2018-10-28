

 # # importing the requests library 
import requests
import json
  
# # api-endpoint
for i in range(1):
	device_id = "dev_f2a682bc2da14f5bb7043ce5d18faa7f"
	user_id = "usr_f2a682bc2da14f5bb7043ce5d18faa7f"
	URL = "https://n8u32bu2v8.execute-api.us-west-2.amazonaws.com/beta/current-state"
	  
	  
	# # defining a params dict for the parameters to be sent to the API 
	PARAMS = { 'device_id':device_id,
				'user_id':user_id,
				'device_type':"aeroasis_device"
				}
	  
	# # sending get request and saving the response as response object 
	r = requests.get(url = URL,params = PARAMS) 
	# # extracting data in json format 
	data = r.json()
	print(json.dumps(data,indent=4))

	#print(data)
	


