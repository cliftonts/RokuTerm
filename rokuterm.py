#!/usr/bin/env python

#************************************************************
#*                                                          *
#*          RokuTerm - Terminal based Roku control          *
#*                                                          *
#*                 Authored by Gareth France                *
#*                                                          *
#************************************************************

import requests
import urllib2
import urllib
import sys
import time
import os
#import neighbourhood


ip = ""
version = "0.0.4"

def help():
	print "************************************************************"
	print "*                                                          *"
	print "*          RokuTerm - Terminal based Roku control          *"
	print "*                                                          *"
	print "*                 Authored by Gareth France                *"
	print "*                           " + version + "                          *"
	print "*                                                          *"
	print "************************************************************"
	print
	print "Usage:"
	print "Load rokuterm, autoscanning for devices."
	print "rokuterm"
	print
	print "Load rokuterm using a specific IP address"
	print "rokuterm --ip=<ip address>"
	print "e.g.: rokuterm 192.168.0.5"
	print
	print "Using the autoscan option is currently very slow and only detects one roku. Additional devices will be ignored."
	print "Only the IP range 192.168.0.xxx is currently scanned. A more versatile scan is currently being developed.
	print "RokuTerm is loosely based upon uRoku for Ubuntu Touch"
	print "https://github.com/ShaneQful/uRoku"
	quit()
	
def send(url):
	payload = {'': ''}
	try:
		# POST with form-encoded data
		r = requests.post(url, data=payload)
		
		# Response, status etc
		#r.text
		#r.status_code
	except:
		print "ROKU NOT FOUND!"

def find():
	global ip
	for i in range(1,256):
		try:
			url = 'http://192.168.0.' + str(i) + ':8060'
			print "Attempting - 192.168.0." + str(i)	
			r = urllib2.urlopen(url)
			html=r.read()
			if "Roku" in html:
				print "Roku found!"
				print "192.168.0." + str(i)
				ip = "192.168.0." + str(i)
				break
		except:
			ip = ""


def keyboard(ip):
	#urllib.quote('/test', safe='')

	#networkCall("POST", "http://" + ip + ":8060/keypress/Backspace");
	keyin = raw_input("Search: ")
	for i in keyin:
		url = "http://" + ip + ":8060/keypress/Lit_" + urllib.quote(i, safe='');
		payload = {'': ''}
		try:
			# POST with form-encoded data
			r = requests.post(url, data=payload)
			
			# Response, status etc
			#r.text
			#r.status_code
		except:
			print "ROKU NOT FOUND!"
		time.sleep(0.1)

#Main
#neighbourhood.main()
#quit()
if len(sys.argv) > 1:
	if "--h" in sys.argv or "--help" in sys.argv:
		help()
	else:
		ip = sys.argv[1]

else:
	find()

if ip == "":
	print "ROKU NOT FOUND!"
	quit()

os.system('cls' if os.name == 'nt' else 'clear')
print " ******** ********** *********** **********"
print " *  7   * *   8    * *    9    * *   /    *"
print " * Back * *   UP   * *  Home   * *  Play  *"
print " ******** ********** *********** **********"
print ""
print " ******** ********** *********** **********"
print " *  4   * *   5    * *    6    * *   *    *"
print " * Left * * Select * *  Right  * * Reload *"
print " ******** ********** *********** **********"
print ""
print " ******** ********** *********** **********"
print " *  1   * *   2    * *    3    * *   -    *"
print " * Rev  * *  Down  * * Forward * *  Quit  *"
print " ******** ********** *********** **********"
print ""
print "          **********"
print "          *   S    *"
print "          * Search *"
print "          **********"

while True:
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

	if key == '9':
		cmd = "http://" + ip + ":8060/keypress/Home"
		send(cmd)
	elif key == '1':
		cmd = "http://" + ip + ":8060/keypress/Rev"
		send(cmd)
	elif key == '3':
		cmd = "http://" + ip + ":8060/keypress/Fwd"
		send(cmd)
	elif key == '*':
		cmd = "http://" + ip + ":8060/keypress/InstantReplay"
		send(cmd)
	elif key == '7':
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
	elif key == '/':
		cmd = "http://" + ip + ":8060/keypress/Play"
		send(cmd)
	elif key == '-':
		quit()
	elif key == 's' or key == 'S':
		keyboard(ip)
	else:
		print "INVALID ENTRY! TRY AGAIN"



