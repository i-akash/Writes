import requests


user='natas11'
Pass='U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
url ='http://%s.natas.labs.overthewire.org/'%user

session=requests.Session()
response=session.get(url,auth = (user,Pass),cookies = {"data": " ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"})
content=response.text
print (content)

#EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
