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
        if count > 3:
            break
    make_a_file(my_list, 'noticesNSU')

def sendmessage(title, message):

    # initialise the d-bus connection
    notify2.init("News Notifier")

    # create Notification object
    n = notify2.Notification(None)

    n.update(title, message)

    # show notification on screen
    n.show()
    return

def make_a_file(my_list,listName):
    with open('/home/sarkerrabi/Desktop/NSUnotices/'+listName+'.csv', 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)

print('\nNorth South University\n')
nsu_top10_notice()