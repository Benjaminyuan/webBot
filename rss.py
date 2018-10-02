import requests
import time
import os
from bs4 import BeautifulSoup
import re
import json
import csv
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
    soup = BeautifulSoup(content)
    container=[]
    for ele in soup.find_all('item'):
        titles = ele.find('title')
        title = titles.string
        des = ele.find('description').string
        url  = ele.find('enclosure')['url']
    #     cast = ele.find('p',{'class':'pl'}).string
    #     remark = ele.find('span',{'class':'rating_nums'}).string.strip()
    #     remarkPeople = ele.find('span',{'class':'pl'}).string
        temp = [title,des,url]
        container.append(temp)
    return container
class title_ob():
    def __init__(self, title, des,url):
        self.url = url
        self.title = title
        self.url = url
            
if __name__=='__main__':
    url = 'https://www.etw.fm/rss'
    content = film_spider(url,0)
    # print(content)
    reslut = get_Data(content)
    i = 1
    #with open('rss.json','w') as fs:
    all_dic = {}
    temp = {}
    index = 1
    content_csv = open('rss.csv',"w",encoding='utf-8')
    write  = csv.writer(content_csv)
    write.writerow(['title','des','url','index'])
    for item in reslut:
        temp.update({'title':item[0],'des':item[1],'src':item[2]})
        write.writerow([item[0],item[1],item[2],index])
        print(f'标题：{item[0]}，des：{item[1]},url:{item[2]}')
        print('\n\n')
        print('-----------------------')
        print(temp)
        all_dic['title'+str(index)] = temp
        temp={}
        index+=1
    print(all_dic)
    print(type(all_dic))
    print(type(json.dumps(all_dic)))
    with open('rss.json','w',encoding='utf-8') as f:
        content_json= json.dumps(all_dic)
        json.dump(content_json,f)
        f.write('\n')
    f.close()