import requests
import random
import os
import string
import json
import time

email_domain = ["@hotmail.com", "@gmail.com", "@outlook.com", "@yahoo.com"]

url = 'http://www.universalstudiospromos.com/happybirthday/regNow.php'

random.seed = (os.urandom(1024)) 

names = json.loads(open('names.json').read())



for name in names:
	time.sleep(5)    #5 second delay was necessary to keep it from crashing
	#name_extra = ''.join(random.choice(string.digits))  #concatenate a random number
	name_extra = ''.join(random.choice(names))	     #concatenate a radnom name	
	email = name.lower() + name_extra + email_domain[random.randrange(0,4)]
	requests.post(url, allow_redirects=False, data={
		'name' : name, 
		'email' : email
	})

	print ('Sending name:', name, 'email:', email) 
