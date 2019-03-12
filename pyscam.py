import requests
import random
import os
import string
import json
import time

email_domain = ["@hotmail.com", "@gmail.com", "@outlook.com", "@yahoo.com"]   #added for more variation amongst emails

url = 'http://www.universalstudiospromos.com/happybirthday/regNow.php'

random.seed = (os.urandom(1024)) 

names = json.loads(open('names.json').read())



for name in names:
	time.sleep(4)    #Delay the frequency of requests to prevent crashing
	num = ''.join(random.choice(string.digits)) + str(random.randrange(0,999)) 
	name_extra = ''.join(random.choice(names))	   	
	email = name.lower() + name_extra + num + email_domain[random.randrange(0,4)]  #revised to descrease liklihood of collision of real email
	requests.post(url, allow_redirects=False, data={
		'name' : name, 
		'email' : email
	})

	print ('Sending name:', name, 'email:', email) 
