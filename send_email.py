from credentials import mailgun_auth
import requests

def send_simple_message(emails):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox3a7d94c7bd064e88ae1d46eb88ec16f3.mailgun.org/messages",
		auth=("api", mailgun_auth),
		data={"from": "Shuai Hao <mailgun@sandbox3a7d94c7bd064e88ae1d46eb88ec16f3.mailgun.org>",
			"to": emails,
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})

if __name__ == '__main__':
	f = open("test_email.txt", "r")
	emails = f.readlines()
	emails = [line.rstrip('\n') for line in emails]
	# print(emails)
	send_simple_message(emails)