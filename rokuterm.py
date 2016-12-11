#networkCall("POST", "http://" + ip + ":8060/keypress/" + id);
import requests

ip = "192.168.0.8"

def send(url):
	#url = 'http://192.168.0.8:8060/keypress/Right'
	payload = {'': ''}

	# GET
	#r = requests.get(url)

	# GET with params in URL
	#r = requests.get(url, params=payload)

	# POST with form-encoded data
	r = requests.post(url, data=payload)
	
	# POST with JSON 
	#import json
	#r = requests.post(url, data=json.dumps(payload))

	# Response, status etc
	#r.text
	#r.status_code

	#print r.status_code

while True:
	print "1. Play"
	print "2. Down"
	print "3. Quit"
	print "4. Left"
	print "5. Select"
	print "6. Right"
	print "7. Home"
	print "8. Up"
	print "9. Back"

        #"InstantReplay": "InstantReplay",
        #"Info":"Info",
        #"Rev":"Rev",
        #"Fwd":"Fwd",
        #"Keyboard":"Keyboard",
        #"IssueWithContacting": "Sorry there appears to have been an issue contacting your roku!",
        #"Apps": "Apps",
        #"TypeWhatYouWant": "Type what you want send to the roku here ..",
        #"Close": "Close",
        #"NotFound":"No Roku Found",
        #"EnterIP":"Enter the ip of your roku here ..",
        #"Save": "Save"
	key = raw_input("Choose:")

	if key == '7':
		cmd = "http://" + ip + ":8060/keypress/Home"
		send(cmd)
	elif key == '9':
		cmd = "http://" + ip + ":8060/keypress/Back"
		send(cmd)
	elif key == '4':
		cmd = "http://" + ip + ":8060/keypress/Left"
		send(cmd)
	elif key == '6':
		cmd = "http://" + ip + ":8060/keypress/Right"
		send(cmd)
	elif key == '8':
		cmd = "http://" + ip + ":8060/keypress/Up"
		send(cmd)
	elif key == '2':
		cmd = "http://" + ip + ":8060/keypress/Down"
		send(cmd)
	elif key == '5':
		cmd = "http://" + ip + ":8060/keypress/Select"
		send(cmd)
	elif key == '1':
		cmd = "http://" + ip + ":8060/keypress/Play"
		send(cmd)
	elif key == '3':
		quit()
	else:
		print "INVALID ENTRY! TRY AGAIN"

	print cmd




