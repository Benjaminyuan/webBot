# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy import Request
from Douban.items import  DoubanItem
class DoubanSpider(scrapy.Spider):
    name = 'douBan'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/latest?icn=index-latestbook-all','https://book.douban.com/chart?subcat=I','https://book.douban.com/chart?subcat=F']

    def parse_book(self,response):
        item = DoubanItem()
        item['publish'] = response.xpath(u'//span[contains(./text(), "出版社:")]/following::text()[1]').extract()[0]
        item['publish_time'] = response.xpath(u'//span[contains(./text(), "出版年:")]/following::text()[1]').extract()[0]
        item['decorate'] = response.xpath(u'//span[contains(./text(), "装帧:")]/following::text()[1]').extract()[0]
        item['ISBN'] = response.xpath(u'//span[contains(./text(), "ISBN:")]/following::text()[1]').extract()[0]
        item['price'] = response.xpath(u'//span[contains(./text(), "定价:")]/following::text()[1]').extract()[0]       
        item['page_num'] = response.xpath(u'//span[contains(./text(), "页数:")]/following::text()[1]').extract()[0]
        writerList = response.xpath('//div[@id="info"]/span/a/text()').extract()
        item['writer'] = writerList[0]
        try:   
            item['translator']  = writerList[1]
        except:
            item['translator'] = '无'    
        yield item   
    def parse(self, response):
        #le = LinkExtractor(restrict_xpaths='//ul/li/div/h2')
        
        urls = response.xpath('//ul/li/div/h2/a/@href')
        #print(urls.extract())
        for url in urls.extract():
            yield Request(url,callback=self.parse_book)
  