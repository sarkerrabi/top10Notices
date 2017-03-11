import urllib.request
from bs4 import BeautifulSoup


def nsu_top10_notice():
    url = 'http://www.northsouth.edu/nsu-announcements/?anaunc_start=0'
    source_code = urllib.request.urlopen(url)

    soup = BeautifulSoup(source_code.read(), "html.parser")
    count = 1
    for title in soup.find_all('h3'):
        print(str(count) + ' ' + title.text)
        for link in title.find_all('a'):
            print('http://www.northsouth.edu/' + link.get('href'))
            count += 1
        if count >= 11:
            break


def aiub_top10_notice():
    url = 'http://www.aiub.edu/'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), "html.parser")
    cnt = 1
    for li in soup.find_all('div', {'class': 'bs-callout'}):
        for link in li.find_all('a'):
            print(str(cnt) + ' ' + link.text)
            print('http://www.aiub.edu' + link.get('href'))
            cnt += 1
        if cnt >= 11:
            break


def bracu_top10_notice():
    url = 'http://www.bracu.ac.bd/news-archive?field_news_department_tid_selective=46'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), "html.parser")
    count = 1
    for linkdiv in soup.find_all('div', {'class': 'field-content title'}):
        for link in linkdiv.find_all('a'):
            print(str(count) + ' ' + link.text)
            print("http://www.bracu.ac.bd" + link.get('href'))
            count += 1
        if count >= 11:
            break


def ewu_top10_notice():
    url = 'http://www.ewubd.edu/category/news/'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), "html.parser")
    count = 1
    for link in soup.find_all('a', {'class': 'post_list_item_title h3'}):

        print(str(count) + ' ' + link.text)
        print(link.get('href'))
        count += 1
        if count >= 11:
            break


def iub_top10_notice():
    url = 'http://www.iub.edu.bd/'
    sour_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(sour_code.read(), "html.parser")
    count = 1
    link_div = soup.find('div', {'class': 'col-lg-5 resources'})
    for link in link_div.find_all('a'):
        print(str(count) + ' ' + link.text)
        print(link.get('href'))
        count += 1
        if count >= 11:
            break


def iubat_top10_notice():
    url = 'http://iubat.edu/web1/index.php/notice/'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), "html.parser")

    link_div1 = soup.find('section', {'class': 'fusion-columns columns fusion-columns-1 columns-1'})

    link_div2 = soup.find('div', {'class': 'fusion-recent-posts avada-container layout-date-on-side layout-columns-1'})
    count = 1
    for link in link_div2.find_all('a'):
        link1 = link_div1.find('a')
        if link1 != link:
            print(str(count) + ' ' + link.text)
            print(link.get('href'))
            count += 1
            if count >= 11:
                break


def uiu_top10_notices():
    url = 'http://www.uiu.ac.bd/notices/'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), 'html.parser')
    count = 1
    for souplink in soup.find_all('h2', {'class': 'entry-title'}):
        link = souplink.find('a')
        print(str(count) + ' ' + link.text)
        print(link.get('href'))
        count += 1
        if count >= 11:
            break


print('\nNorth South University\n')
nsu_top10_notice()
print('\nAmerican International University Bangladesh\n')
aiub_top10_notice()
print('\nBRAC University\n')
bracu_top10_notice()
print('\nEast West University\n')
ewu_top10_notice()
print('\nIndependent University, Bangladesh\n')
iub_top10_notice()
print('\nIUBAT— International University of Business Agriculture and Technology\n')
iubat_top10_notice()
print("\nUnited International University\n")
uiu_top10_notices()
