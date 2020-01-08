from credentials import github_token
import requests
import pandas as pd
import csv
import json
import time

def scrape_email(url):
	data = requests.get(url).text
	user_json = json.loads(data)
	try:
		login = user_json['login']
		email = user_json['email']

		return (login, email)
	except:
		if user_json['message'] == "Not Found":
			return ('','')
		else:
			print(user_json)



if __name__ == '__main__':
	f = open("stargazers_profile.txt", "r")
	urls = f.readlines()
	urls = [(line.rstrip('\n') + '?access_token=' + github_token) for line in urls]
	# urls = urls[38500:]
	# print(len(urls))
	name_list = []
	email_list = []
	count = 0
	for url in urls:
		count += 1
		login, email = scrape_email(url)
		name_list.append(login)
		email_list.append(email)
		if count % 1000 == 0:
			print(count)
			df = pd.DataFrame(list(zip(name_list, email_list)), columns=['Login', 'Email'])
			df.to_csv("stargazers_profile2.csv", index=False, encoding='utf-8')

	df = pd.DataFrame(list(zip(name_list, email_list)), columns=['Login', 'Email'])
	df.to_csv("stargazers_profile2.csv", index=False, encoding='utf-8')