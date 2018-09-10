import requests
import time
import os
from bs4 import BeautifulSoup
import re
#一些头部信息
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]
def film_spider(url,i):
    try:
        r = requests.get(url,headers=hds[i])
        r.encoding = 'utf-8'
        r.raise_for_status()
        return r.text
    except:
        pass
def get_Data(content):
    soup = BeautifulSoup(content,'lxml')
    container=[]
    for ele in soup.find_all('div',{'class':'pl2'}):
        names = ele.find('a')
        name = names.get_text()
        # try:
        #     otherName = names.find('span').string
        # except:
        #    otherName = ''
        cast = ele.find('p',{'class':'pl'}).string
        remark = ele.find('span',{'class':'rating_nums'}).string.strip()
        remarkPeople = ele.find('span',{'class':'pl'}).string
        temp = [name,cast,remark,remarkPeople]
        container.append(temp)
    return container
if __name__=='__main__':
    url = 'https://movie.douban.com/chart'
    content = film_spider(url,0)
    reslut = get_Data(content)
    i = 1
    for item in reslut:
        print('Top{0:2}:{1:40}\n\n{2:10}\n\n{3:40}'.format(i,re.sub(r'[\s\t]','',item[0])\
        ,item[1],item[2]+item[3]))
        print('----------------------------')
        i+=1