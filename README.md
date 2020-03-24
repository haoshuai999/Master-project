## Master's Project
My master's project is a data story about the overwork problem of Chinese programmers. A lot of Chinese tech companies require their employees to work from 9 am to 9 pm, six days a week, and programmers call the schedule the "996" work schedule. In spring 2019, the "anti-996" online movement gets the world's attention. Chinese programmers protested on GitHub and maintained a blacklist of "996" companies. Although the movement led to a discussion about work and life balance, the overwork problem didn't get better.  

The code in this repository is used to send questionnaires to Chinese programmers who starred [the "996.ICU" GitHub repository](https://github.com/996icu). The email addresses were scraped from the GitHub API.

- The script "email_address.py" was used to scrape email addresses in [the dataset](https://github.com/Alfred1984/interesting-python) of GitHub user "Alfred1984"
- The script "stargazers.py" was used to scrape email addresses directly from GitHub API
- The script "compare.py" was used to get the unique email addresses after merge the above two sources
- The script "validate_stargazers_email" was used to validate the email addresses
- The script "send_email.py" was used to send email
- The Jupyter notebook "Master_Project_viz.ipynb" was used to visualize the survey data