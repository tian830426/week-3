import requests
from bs4 import BeautifulSoup
import time

def pttMovie(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤：' + url)
        return
    
    soup = BeautifulSoup(resp.text, 'html5lib')

    paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']
    print('paging:',paging)
    
    titles = [] 
    rents = soup.find_all('div', 'r-ent')
    for rent in rents:
        title = rent.find('div', 'title').text.strip()  
        a = ['[好雷]','[普雷]','[負雷]']
        for item in a:
            if item in title  and not "Re" in title:
                titles.append(title)
    print(titles)
    
    return_d = dict()
    return_d['paging'] = paging
    return_d['title'] = titles
    return(return_d)

all_title=[]
for i in range(0,10):
    if i == 0:
        output = pttMovie('https://www.ptt.cc/bbs/movie/index.html')
    else:
        all_title.extend(output['title'])
        print(i)
        output = pttMovie('https://www.ptt.cc' + output['paging'])