import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = 'yourdb.com'
PASSWORD = os.getenv('DB_PASSWORD')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')

if PASSWORD is None or SECRET_TOKEN is None:
    raise ValueError(
        " Either the .env file is missing OR"
        f" one of the variables PASSWORD or SECRET_TOKEN has not been set in .env file")
print('You Password is',PASSWORD)
print('You Secret Token is',SECRET_TOKEN)


## References
# https://towardsdatascience.com/using-dotenv-to-hide-sensitive-information-in-python-77ab9dfdaac8
# https://towardsdatascience.com/stop-hardcoding-sensitive-data-in-your-python-applications-86eb2a96bec3
# https://studygyaan.com/django/how-to-protect-sensitive-data-in-django