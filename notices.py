import urllib.request
from bs4 import BeautifulSoup
def nsu_top10_notice():
    url ='http://www.northsouth.edu/nsu-announcements/?anaunc_start=0'
    source_code = urllib.request.urlopen(url)

    soup = BeautifulSoup(source_code.read(),"html.parser")
    count=1
    for title in soup.find_all('h3'):
        print(str(count)+' '+title.text)
        for link in title.find_all('a'):
            print('http://www.northsouth.edu/'+link.get('href'))
            count+=1
        if (count >= 11):
            break
def aiub_top10_notice():
    url ='http://www.aiub.edu/'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(),"html.parser")
    cnt = 1
    for li in soup.find_all('div',{'class':'bs-callout'}):
        for link in li.find_all('a'):
            print(str(cnt)+' '+link.text)
            print('http://www.aiub.edu'+link.get('href'))
            cnt += 1
        if (cnt >= 11):
            break
def bracu_top10_notice():
    url ='http://www.bracu.ac.bd/news-archive?field_news_department_tid_selective=46'
    source_code=urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(),"html.parser")
    count =1
    for linkdiv in soup.find_all('div',{'class':'field-content title'}):
        for link in linkdiv.find_all('a'):
            print(str(count)+' '+link.text)
            print("http://www.bracu.ac.bd"+link.get('href'))
            count+=1
        if (count >= 11):
            break


print('\nNorth South University')
nsu_top10_notice()
print('\nAIUB')
aiub_top10_notice()
print('\nBRACU')
bracu_top10_notice()