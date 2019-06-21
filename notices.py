import urllib.request

import notify2
from bs4 import BeautifulSoup
def nsu_top10_notice():
    url = 'http://www.northsouth.edu/nsu-announcements/?anaunc_start=0'
    source_code = urllib.request.urlopen(url)

    soup = BeautifulSoup(source_code.read(), "html.parser")
    count = 1
    my_list = []
    for link in soup.find_all('a',{'class': 'post-title-mini main-color-1-hover'}):
        print(str(count) + ' ' + link.text)
        print('http://www.northsouth.edu/' + link.get('href'))
        sendmessage(str(count) + ' ' + link.text, 'http://www.northsouth.edu/' + link.get('href'))
        my_list.append(str(count) + ' ' + link.text)
        my_list.append('http://www.northsouth.edu/' + link.get('href'))
        count += 1
        if count > 10:
            break
    make_a_file(my_list, 'noticesNSU')


def aiub_top10_notice():
    url = 'http://www.aiub.edu/'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), "html.parser")
    cnt = 1
    my_list = []
    for li in soup.find_all('div', {'class': 'bs-callout'}):
        for link in li.find_all('a'):
            print(str(cnt) + ' ' + link.text)
            print('http://www.aiub.edu' + link.get('href'))
            my_list.append(str(cnt) + ' ' + link.text)
            my_list.append('http://www.aiub.edu' + link.get('href'))
            cnt += 1
        if cnt > 10:
            break


def bracu_top10_notice():
    url = 'http://www.bracu.ac.bd/news-archive?field_news_department_tid_selective=46'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), "html.parser")
    count = 1
    my_list = []
    for linkdiv in soup.find_all('div', {'class': 'field-content title'}):
        for link in linkdiv.find_all('a'):
            print(str(count) + ' ' + link.text)
            print("http://www.bracu.ac.bd" + link.get('href'))
            my_list.append(str(count) + ' ' + link.text)
            my_list.append('http://www.bracu.ac.bd' + link.get('href'))
            count += 1
        if count > 10:
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
        if count > 10:
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
        if count > 10:
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
            if count > 10:
                break


def uiu_top10_notices():
    url = 'http://www.uiu.ac.bd/notices/'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), 'html.parser')
    count = 1
    my_list = []
    for souplink in soup.find_all('h2', {'class': 'entry-title'}):
        link = souplink.find('a')
        print(str(count) + ' ' + link.text)
        print(link.get('href'))
        my_list.append(str(count) + ' ' + link.text)
        my_list.append(link.get('href'))
        count += 1
        if count > 10:
            break
    make_a_file(my_list,'noticesUIU')



def seu_top10_notices():
    url = 'http://www.seu.ac.bd/notice_board.php'
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code.read(), 'html.parser')
    count = 1
    for link in soup.find_all('a', {'rel': 'facebox'}):
        print(str(count) + ' ' + link.text)
        print(url + link.get('href'))
        count += 1
        if count > 10:
            break




def sendmessage(title, message):

    # initialise the d-bus connection
    notify2.init("News Notifier")

    # create Notification object
    n = notify2.Notification(None)

    n.update(title, message)

    # show notification on screen
    n.show()
    return

# for making a file for notices
def make_a_file(my_list,listName):
    with open(listName+'.csv', 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)


print("\nUnited International University\n")
uiu_top10_notices()
print('\nEast West University\n')
ewu_top10_notice()
print('\nIndependent University, Bangladesh\n')
iub_top10_notice()
print('\nNorth South University\n')
nsu_top10_notice()


# print('\nAmerican International University Bangladesh\n')
# aiub_top10_notice()
# print('\nBRAC University\n')
# bracu_top10_notice()
# print('\nInternational University of Business Agriculture and Technology\n')
# iubat_top10_notice()
# print("\nSoutheast University\n")
# seu_top10_notices()
