from bs4 import BeautifulSoup as soup
from urllib.request import  urlopen as ureq


url='https://www.facebook.com/'
uclient=ureq(url)
page_html=uclient.read()
uclient.close()
page_soup=soup(page_html,"html.parser")

print (page_soup.h1)
