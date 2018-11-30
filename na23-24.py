import requests
from string import *

username='natas23'
password='D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'
url='http://natas23.natas.labs.overthewire.org/'
session=requests.Session()

response=session.post(url,data={"passwd" : "100iloveyou"},auth=(username,password))
print response.text
print "="*80


#OsRmXFguozKpTZZ5X14zNO43379LZveg
