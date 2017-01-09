#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#************************************************************
#*                                                          *
#*          RokuTerm - Terminal based Roku control          *
#*                                                          *
#*                 Authored by Gareth France                *
#*                                                          *
#************************************************************

import requests
import urllib
import sys, termios, atexit
import time
import os
from select import select
if sys.version_info >= (3,0):
	import urllib.request
else:
	import urllib2
#import neighbourhood


ip = ""
version = "0.2.2"

#KB hit routines START
# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def putch(ch):
    sys.stdout.write(ch)

def getch():
    return sys.stdin.read(1)

def getche():
    ch = getch()
    putch(ch)
    return ch

def kbhit():
    dr,dw,de = select([sys.stdin], [], [], 0)
    #return dr <> []
    return dr != []
	
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
    screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()	

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())	
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
class _GetchWindows:

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
#KB Hit routines END

def menu():
	#try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print (u'\u2554' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2564' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2564' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2557')
	print (u'\u2551' + "   7   " + u'\u2502' + "   8   " + u'\u2502' + "   9   " + u'\u2551')
	print (u'\u2551' + " Back  " + u'\u2502' + "  Up   " + u'\u2502' + " Home  " + u'\u2551')
	print (u'\u255F' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u253C' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u253C' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2562')
	
	print (u'\u2551' + "   4   " + u'\u2502' + "   5   " + u'\u2502' + "   6   " + u'\u2551')
	print (u'\u2551' + " Left  " + u'\u2502' + "Select " + u'\u2502' + " Right " + u'\u2551')
	print (u'\u255F' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u253C' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u253C' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2562')
	
	print (u'\u2551' + "   1   " + u'\u2502' + "   2   " + u'\u2502' + "   3   " + u'\u2551')
	print (u'\u2551' + "  Rev  " + u'\u2502' + " Down  " + u'\u2502' + "Forward" + u'\u2551')
	print (u'\u255F' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u253C' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u253C' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2562')
	
	print (u'\u2551' + "   /   " + u'\u2502' + "   *   " + u'\u2502' + "   -   " + u'\u2551')
	print (u'\u2551' + " Play  " + u'\u2502' + "Reload " + u'\u2502' + " Quit  " + u'\u2551')
	print (u'\u255F' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u253C' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u253C' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2500' + u'\u2562')
	
	print (u'\u2551' + "   0   " + u'\u2502' + "   S   " + u'\u2502' + "       " + u'\u2551')
	print (u'\u2551' + " Info  " + u'\u2502' + "Search " + u'\u2502' + "       " + u'\u2551')
	print (u'\u255A' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2567' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2567' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u2550' + u'\u255D')
	#except:
	#	os.system('cls' if os.name == 'nt' else 'clear')
	#	print (" ******** ********** *********** **********")
	#	print (" *  7   * *   8    * *    9    * *   /    *")
	#	print (" * Back * *   UP   * *  Home   * *  Play  *")
	#	print (" ******** ********** *********** **********")
	#	print ("")
	#	print (" ******** ********** *********** **********")
	#	print (" *  4   * *   5    * *    6    * *   *    *")
	#	print (" * Left * * Select * *  Right  * * Reload *")
	#	print (" ******** ********** *********** **********")
	#	print ("")
	#	print (" ******** ********** *********** **********")
	#	print (" *  1   * *   2    * *    3    * *   -    *")
	#	print (" * Rev  * *  Down  * * Forward * *  Quit  *")
	#	print (" ******** ********** *********** **********")
	#	print ("")
	#	print (" ******** **********")
	#	print (" *  0   * *   S    *")
	#	print (" * Info * * Search *")
	#	print (" ******** **********")

def help():
	print ("************************************************************")
	print ("*                                                          *")
	print ("*          RokuTerm - Terminal based Roku control          *")
	print ("*                                                          *")
	print ("*                 Authored by Gareth France                *")
	print ("*                           " + version + "                          *")
	print ("*                                                          *")
	print ("************************************************************")
	print ("")
	print ("Usage:")
	print ("Load rokuterm, autoscanning for devices.")
	print ("rokuterm")
	print ("")
	print ("Load rokuterm using a specific IP address")
	print ("rokuterm --ip=<ip address>")
	print ("e.g.: rokuterm 192.168.0.5")
	print ("")
	print ("Using the autoscan option is currently very slow and only detects one roku.")
	print ("Additional devices will be ignored.")
	print ("Only the IP range 192.168.0.xxx is currently scanned. A more versatile scan")
	print ("is currently being developed.")
	print ("RokuTerm is loosely based upon uRoku for Ubuntu Touch")
	print ("https://github.com/ShaneQful/uRoku")
	print ("")
	donate()
	
def send(url):
	payload = {'': ''}
	try:
		# POST with form-encoded data
		r = requests.post(url, data=payload)
		
		# Response, status etc
		#r.text
		#r.status_code
	except:
		print ("ROKU NOT FOUND!")

def find():
	global ip
	for i in range(1,256):
		try:
			url = 'http://192.168.0.' + str(i) + ':8060'
			print ("Attempting - 192.168.0." + str(i))	
			r = urllib2.urlopen(url)
			html=r.read()
			if "Roku" in html:
				print ("Roku found!")
				print ("192.168.0." + str(i))
				ip = "192.168.0." + str(i)
				break
		except:
			ip = ""

def donate():
	print ("If you have found RokuTerm useful please consider making a small donation to")
	print ("fund future development.")
	print ("Paypal:- gareth.france@gmail.com")
	print ("PPPay.com:- gareth.france@cliftonts.co.uk")
	print ("")
	print ("A massive thank you to kyrofa, elopio and Mark Shuttleworth for their help")
	print ("in making the snap version possible.")
	os.system('setterm -cursor on')
	quit()



def keyboard(ip):
	#urllib.quote('/test', safe='')

	#networkCall("POST", "http://" + ip + ":8060/keypress/Backspace");
	#if sys.version_info < (3,0):
	set_normal_term()
	if sys.version_info >= (3,0):
		keyin = input("Search: ")
	else:
		keyin = raw_input("Search: ")
	for i in keyin:
		if sys.version_info >= (3,0):
			url = "http://" + ip + ":8060/keypress/Lit_" + urllib.parse.quote(i, safe='');
		else:
			url = "http://" + ip + ":8060/keypress/Lit_" + urllib.quote(i, safe='');
		payload = {'': ''}
		try:
			# POST with form-encoded data
			r = requests.post(url, data=payload)
			
			# Response, status etc
			#r.text
			#r.status_code
		except:
			print ("ROKU NOT FOUND!")
		time.sleep(0.2)
	#if sys.version_info < (3,0):
	set_curses_term()
	menu()

#Main
#neighbourhood.main()
#quit()
os.system('setterm -cursor off')
atexit.register(set_normal_term)
set_curses_term()

if len(sys.argv) > 1:
	if "--h" in sys.argv or "--help" in sys.argv:
		help()
	else:
		ip = sys.argv[1]

else:
	find()

if ip == "":
	print ("ROKU NOT FOUND!")
	os.system('setterm -cursor on')
	quit()

key = ""
menu()

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
	#if sys.version_info >= (3,0):
	#	key = input("Choose:")
	#else:
	#	key = raw_input("Choose:")
	if kbhit():
		key = getch()
	
	if key == '9':
		cmd = "http://" + ip + ":8060/keypress/Home"
		send(cmd)
		key = ""
	elif key == '1':
		cmd = "http://" + ip + ":8060/keypress/Rev"
		send(cmd)
		key = ""
	elif key == '3':
		cmd = "http://" + ip + ":8060/keypress/Fwd"
		send(cmd)
		key = ""
	elif key == '*':
		cmd = "http://" + ip + ":8060/keypress/InstantReplay"
		send(cmd)
		key = ""
	elif key == '7':
		cmd = "http://" + ip + ":8060/keypress/Back"
		send(cmd)
		key = ""
	elif key == '4':
		cmd = "http://" + ip + ":8060/keypress/Left"
		send(cmd)
		key = ""
	elif key == '6':
		cmd = "http://" + ip + ":8060/keypress/Right"
		send(cmd)
		key = ""
	elif key == '8':
		cmd = "http://" + ip + ":8060/keypress/Up"
		send(cmd)
		key = ""
	elif key == '2':
		cmd = "http://" + ip + ":8060/keypress/Down"
		send(cmd)
		key = ""
	elif key == '5':
		cmd = "http://" + ip + ":8060/keypress/Select"
		send(cmd)
		key = ""
	elif key == '/':
		cmd = "http://" + ip + ":8060/keypress/Play"
		send(cmd)
		key = ""
	elif key == '0':
		cmd = "http://" + ip + ":8060/keypress/Info"
		send(cmd)
		key = ""
	elif key == '-':
		os.system('cls' if os.name == 'nt' else 'clear')
		donate()
	elif key == 's' or key == 'S':
		keyboard(ip)
		key = ""

