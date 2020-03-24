# coding=utf8
from credentials import mailgun_auth
import requests
from datetime import datetime, timedelta
import time

def send_simple_message(email):
	return requests.post(
		"https://api.mailgun.net/v3/996.haoshuai.online/messages",
		auth=("api", mailgun_auth),
		data={"from": "Shuai Hao <mailgun@sandbox3a7d94c7bd064e88ae1d46eb88ec16f3.mailgun.org>",
			"to": email,
			"subject": "***",
			"text": "***",
			"html": "***"
			})

if __name__ == '__main__':
	f = open("stargazers_email.txt", "r")
	emails = f.readlines()
	emails = [line.rstrip('\n') for line in emails]


	i = 0
	while 1:
		print("Email list: %d to %d" % (100 * i + 14922, 100 * i + 14923))
		selected_email = emails[(100 * i + 14922) : (100 * i + 14923)]
		for email_address in selected_email:
			send_simple_message(email_address)
		i += 1

		dt = datetime.now() + timedelta(hours=1)
		print(dt)
		# dt = dt.replace(minute=10)

		while datetime.now() < dt:
			time.sleep(1)