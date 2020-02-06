# coding=utf8
from validate_email import validate_email

if __name__ == '__main__':
	f = open("stargazers_email.txt", "r")
	emails = f.readlines()
	emails = [line.rstrip('\n') for line in emails]
	valid_email = []

	for i in range(len(emails)):
		is_valid = validate_email(emails[i], verify=True)
		print(is_valid)
		if is_valid == 'True':
			valid_email.append(emails[i])

	print(len(valid_email))
	with open('valid_email.txt', 'w') as f:
		for item in valid_email:
			f.write("%s\n" % item)

