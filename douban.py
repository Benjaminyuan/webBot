import requests
import sys 
import time
import os
from bs4 import BeautifulSoup
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
    for ele in soup.find_all('div',{'class':'info'}):
        names = ele.find_all('span',{'class':'title'})
        name = ''
        for item in names:
            name+=item.string
        remark = ele.find('span',{'class':'rating_num'}).string.strip()
        quote = ele.find('span',{'class':'inq'}).string.strip()
        temp = [name,remark,quote]
        container.append(temp)
    return container
if __name__=='__main__':
    baseurl = 'https://movie.douban.com/top250'
    reslut = []
    for i in range(10):
        url = baseurl +f'?start={i*25}&filter='
        content = film_spider(url,0)
        reslut += get_Data(content)
    i = 1
    for item in reslut:
        print('Top{0:3}:{1:40}\t{2:10}\t{3:40}'.format(i,item[0].replace(' ',''),item[1],item[2]))
        i+=1