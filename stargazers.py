from credentials import github_token
import requests
import json

def scrape(url, users_profile):
	data = requests.get(url).text
	data_json = json.loads(data)
	for user in data_json:
		users_profile.append(user['url'])

if __name__ == '__main__':
	users_profile = []
	per_page = 100
	for page in range(401):
		stargazer_url = "https://api.github.com/repos/996icu/996.ICU/stargazers?page=" + str(page) + "&per_page=" + str(per_page) + "&access_token=" + github_token
		scrape(stargazer_url, users_profile)
		print(len(users_profile))

	with open('stargazers_profile.txt', 'w') as f:
		for item in users_profile:
			f.write("%s\n" % item)