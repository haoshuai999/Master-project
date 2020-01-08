import pandas as pd

original_user = pd.read_csv('users_data.csv')
new_user = pd.read_csv('stargazers_profile_filtered.csv')

orginal_email = list(original_user['email'])
new_email = list(new_user['Email'])

unique_email = set(orginal_email + new_email)
print(len(set(orginal_email)))
print(len(set(new_email)))
print(len(unique_email))

with open('stargazers_email.txt', 'w') as f:
	for item in unique_email:
		f.write("%s\n" % item)