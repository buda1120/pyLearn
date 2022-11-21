"""
Created on Tue Nov 15 16:39:07 2022
爬取 中国大学排名信息并打印
@author: bing
"""
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(str(e))
        return ''

def fillUnivList(ls, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.tbody.children:
        rank = tr('td')[0].string.strip()
        nameCN = tr('td')[1].find('a', 'name-cn').string.strip()
        nameEN = tr('td')[1].find('a', 'name-en').string.strip()
        name = nameCN + '(' + nameEN + ')'
        for str in tr('td')[2].stripped_strings:
            rigion = str
        for str in tr('td')[3].stripped_strings:
            univType = str
        score = tr('td')[4].string.strip()
        item = [rank, name, rigion, univType, score]
        ls.append(item)

def printUnivList(ls, num):
    print('{:4}\t\t{:<65}\t{:<6}\t{:>4}\t{:<}'.format('排名', '学校名称', '地区', '学校类型', '总分', chr(12288)))
    print('-'*126)
    for data in ls[:num]:
        print('{:4}\t{:<71}\t{:<6}\t{:^8}\t{:<}'.format(data[0], data[1], data[2], data[3], data[4], chr(12288)))

if __name__ == '__main__':
    url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
    ls = []
    text = getHTMLText(url)
    fillUnivList(ls, text)
    printUnivList(ls, 30)

