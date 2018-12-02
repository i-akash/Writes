import requests
import bs4
url='https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/'


anch=list()
phrase=list()
dic=dict()
anch.append(url+'qds.html')
dic[url+'qds.html']=1

for ur in anch:
    res=requests.get(ur)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    ph=soup.select("font")
    for p in ph :
        st=p.text
        phrase.append(st[15:])
    al=soup.findAll('a',href=True)
    for link in al:
        l=url+link['href']
        if l not in dic:
            anch.append(l)
            dic[l]=1
phrase.sort()

for p in phrase:
    print(p)
