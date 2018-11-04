import tkinter as tk
from tkinter import *
import requests
import json

device_id = "dev_f2a682bc2da14f5bb7043ce5d18faa7f"
user_id = "usr_f2a682bc2da14f5bb7043ce5d18faa7f"
plant_type = "1"
PARAMS = { 	'user_id':user_id,
			'device_id':device_id,
				'device_type':"aeroasis_device"
				}
GROW_PARAMS = { 'device_id':device_id,
				'user_id':user_id,
				'device_type':"aeroasis_device",
				'plant_type':plant_type,
				}

def req_func(operation):
	URL = "https://n8u32bu2v8.execute-api.us-west-2.amazonaws.com/beta/"+operation
	data = None
	if operation == "current-state" or operation == "end-grow":
		r = requests.get(url = URL,params = PARAMS) 
	elif operation == "start-grow":
		r = requests.post(url = URL, params = GROW_PARAMS, data = data)
	else:
		r = requests.post(url = URL, params = PARAMS, data = data) 
	# # extracting data in json format 
	data = r.json()
	T.delete('1.0', END)
	T.insert(END, json.dumps(data,indent=4))
	return


root = tk.Tk()
root.title("App simulation")
root.geometry("500x500")
S = Scrollbar(root)
T = Text(root, height=25, width=50)
mainframe = tk.Frame(root)
mainframe.grid()
S.grid(column = 40)
T.grid(column = 20, row =0)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)


button1 = tk.Button(mainframe, text="Start Grow", width=15, height=3,background = "lightgrey",activebackground = "#33B5E5",command=lambda:req_func("start-grow")).grid(column=8, row=0, sticky=W)
button2 = tk.Button(mainframe, text="Start Water change", width=15, height=3,background = "lightgrey",activebackground = "#33B5E5",command=lambda:req_func("start-water-change")).grid(column=8, row=2, sticky= W)
button3 = tk.Button(mainframe, text="Start pH dosing", width=15, height=3,background = "lightgrey",activebackground = "#33B5E5", command=lambda:req_func("start-ph-dosing")).grid(column=8, row=3, sticky= W)
button4 = tk.Button(mainframe, text="Start nutrient dosing", width=15, height=3,background = "lightgrey",activebackground = "#33B5E5", command=lambda:req_func("start-nutrient-dosing")).grid(column=8, row=4, sticky= W)
button5 = tk.Button(mainframe, text="Current sensor state", width=15, height=3,background = "lightgrey",activebackground = "#33B5E5", command=lambda:req_func("current-state")).grid(column=8, row=5, sticky= W)
button6 = tk.Button(mainframe, text="End Grow", width=15, height=3,background = "red", command=lambda:req_func("end-grow")).grid(column=8, row=6, sticky =W)


root.mainloop()