# Get_list.py 20210201
# 取得臉書「左轉有活動」內貼文清單
# https://m.facebook.com/groups/1556727317714336/
#

from bs4 import BeautifulSoup
import re
from pprint import pprint

html = open('.\\左轉有活動\\左轉有活動.html', 'r', encoding='utf-8')

r = BeautifulSoup(html, 'lxml')


def get_links(r):
    """ return permalink + events if there is
    """

    href_list = [x.get('href')
                 for x in r.find_all('a')]

    title = r.find('div', class_='_5rgt').find('span')

    link_list = []
    perma_link = []
    events_link = []
    for x in href_list:

        if x is not None and 'permalink' in x:
            perma_link.append(re.search(
                r'^https://m\.facebook\.com/groups/1556727317714336/permalink/\d+/', x).group())
        if x is not None and 'events' in x:
            events = ''
            events_id = ''
            try:
                # https://m.facebook.com/events/feed/watch/?event_id=2107988616120756&amp;
                events = re.search(
                    r'^https://m\.facebook\.com/events/feed/watch/\?event_id=\d+\&', x).group()
                events_id = re.search(r'\d+', events).group()
                events_link.append(
                    'https://m.facebook.com/events/' + events_id)
            except:
                pass

    if perma_link != []:
        link_list.append((title, ''.join(set(perma_link)),
                          ''.join(set(events_link))))
    return link_list


articles_list = [x for x in r.find_all('article')]

# links_list = re.search(r'^https://m.facebook.com/groups/1556727317714336/permalink/\d+/\?', y.get('href')).group()
# event_list = re.search(r'https://m.facebook.com/events/\d+\?', y.get('href')).group()

links_list = [get_links(x) for x in articles_list]
# links_list = [x for x in links_list if x != []]

print(r.title)
print(len(articles_list))
print(len(links_list))
print(links_list)
pprint(links_list[98])
